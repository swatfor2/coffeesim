from coffee_machine_object import order
from coffee_machine_object import BeverageList, BeverageItem
from coffee_machine_object import constants
from DataController import addOrderEntry, getOrderEntries, getLatestStatus, addStatusEntry
from CoffeeMachineScoring import CoffeeMachineScoring
import datetime




class CoffeeMachine(object):

    def __init__(self):
        self.beverageList = BeverageList()
        self._standardBeverages = self.beverageList.getBeverageList()
        self._beverageDict = self.beverageList.getBeverageDict()
        self.coffeeMachineStatus = self._startUp()
        #self.coffeeMachineScoring = CoffeeMachineScoring()

    def _startUp(self):
        #check and get the States of the Machine
        #Request from DB
        #Filled with dummy data
        tempCoffeeMachineStatus = getLatestStatus()

        return tempCoffeeMachineStatus

    def getBeverageList(self, timestamp):
        #List format not defined yet
        if self._checkRecommendationModule():
            scoredBeverages = self._getScoredBeverageList(timestamp)
            for score in scoredBeverages:
                tempBeverage = self._beverageDict.get(str(score[0]))
                tempBeverage["score"] = score[1]
                self._beverageDict[str(score[0])] = tempBeverage
            return self._beverageDict
        else:
            for i in range(len(self._beverageDict)):
                tempBeverage = self._beverageDict.get(str(i + 1))
                tempBeverage["score"] = 0
                self._beverageDict[str(i + 1)] = tempBeverage
            return self._beverageDict

    def orderBeverage(self, beverageID, timestamp):
        if self._checkResources(beverageID):
            self._recalculateResources(beverageID, timestamp)
            newOrder = order.CoffeeMachineOrder("", beverageID, timestamp)
            self._logOrder(newOrder)
            self._logStatus()
            return True
        else:
            return False

    def turnMachineOff(self):
        self.coffeeMachineStatus.energySaver = 0
        self.coffeeMachineStatus.powerOn = 0
        self._logStatus()

    def turnMachineOn(self):
        self.coffeeMachineStatus.energySaver = 0
        self.coffeeMachineStatus.powerOn = 1
        self._logStatus()

    def turnEnergySaferModeOff(self):
        self.coffeeMachineStatus.energySaver = 0
        self.coffeeMachineStatus.powerOn = 1
        self._logStatus()

    def turnEnergySaferModeOn(self):
        self.coffeeMachineStatus.energySaver = 1
        self.coffeeMachineStatus.powerOn = 1
        self._logStatus()

    def fillUpMilk(self):
        self.coffeeMachineStatus.remainingMilk = constants.MAXMILK
        self._logStatus()
        return True

    def fillUpBeans(self):
        self.coffeeMachineStatus.remainingBeans = constants.MAXBEANS
        self._logStatus()
        return True

    def fillUpWater(self):
        self.coffeeMachineStatus.remainingWater = constants.MAXWATER
        self._logStatus()
        return True

    def _checkRecommendationModule(self):
        #Is Recommendation Moduloe is active
        return True
    
    def _getScoredBeverageList(self, timestamp):
        #Request an Recommendation Module
        results = CoffeeMachineScoring.berechnungScore(timestamp)
        return results

    def _checkResources(self, id):
        #if required resources > current resources --> True else False
        #if less than 10% of any resource is available --> call recommendation module
        enoughResourcesAvailable = True

        #Check if enough resources are available for the order
        if (
                self.coffeeMachineStatus.remainingBeans >= self._beverageDict.get(id).get("item").requiredBeans and
                self.coffeeMachineStatus.remainingMilk >= self._beverageDict.get(id).get("item").requiredMilk and
                self.coffeeMachineStatus.remainingWater >= self._beverageDict.get(id).get("item").requiredWater
        ):
            enoughResourcesAvailable = True
        else:
            enoughResourcesAvailable = False

        #Check available Resources and inform recommendation module if necessary
        if self.coffeeMachineStatus.remainingBeans < constants.MAXBEANS * 0.1:
            #Call recommendation module
            self.fillUpBeans()

        if self.coffeeMachineStatus.remainingMilk < constants.MAXMILK * 0.1:
            # Call recommendation module
            # TODO Manage communication with recom. module
            self.fillUpMilk()

        if self.coffeeMachineStatus.remainingWater < constants.MAXWATER * 0.1:
            # Call recommendation module
            self.fillUpWater()

        return enoughResourcesAvailable

    def _recalculateResources(self, id, timestamp):
        #Subtract required resources from current resources
        self.coffeeMachineStatus.powerOn = 1
        self.coffeeMachineStatus.energySaver = 0
        self.coffeeMachineStatus.timestamp = timestamp
        self.coffeeMachineStatus.grinderRuntime += self._beverageDict.get(id).get("item").grinderRuntime
        self.coffeeMachineStatus.id = ""
        self.coffeeMachineStatus.pumpRuntime += self._beverageDict.get(id).get("item").pumpRuntime
        self.coffeeMachineStatus.remainingBeans -= self._beverageDict.get(id).get("item").requiredBeans
        self.coffeeMachineStatus.remainingMilk -= self._beverageDict.get(id).get("item").requiredMilk
        self.coffeeMachineStatus.remainingWater -= self._beverageDict.get(id).get("item").requiredWater
        self.coffeeMachineStatus.machineRuntime += 30

    def _logOrder(self, newOrder):
        #Call DB module and log order
        addOrderEntry(newOrder)

    def _logStatus(self):
        #Call DB module and log order
        addStatusEntry(self.coffeeMachineStatus)
