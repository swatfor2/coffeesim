from CoffeeMachineStatus import CoffeeMachineStatus
from CoffeeMachineOrder import CoffeeMachineOrder
from DataController import addOrderEntry, getOrderEntries, getLatestStatus, addStatusEntry
from Beverage import BeverageList, BeverageItem

import datetime

# Globals
MAXMILK = 1000  # ml
MAXWATER = 2000  # ml
MAXBEANS = 1000  # gramm


class CoffeeMachine(object):

    def __init__(self):
        self.beverageList = BeverageList()
        self._standardBeverages = self.beverageList.getBeverageList()
        self._beverageDict = self.beverageList.getBeverageDict()
        self._scoredBeverages = []
        self.coffeeMachineStatus = self._startUp()

    def _startUp(self):
        #check and get the States of the Machine
        #Request from DB
        #Filled with dummy data
        tempCoffeeMachineStatus = getLatestStatus()

        return tempCoffeeMachineStatus

    def getBeverageList(self):
        #List format not defined yet
        if self._checkRecommendationModule():
            self._scoredBeverages = self._getScoredBeverageList()
            return self._scoredBeverages
        else:
            return self._standardBeverages

    def orderBeverage(self, beverageID, timestamp):
        if self._checkResources(beverageID):
            #self._recalculateResources(beverageID, timestamp) TODO Marek bitte überprüfen.. funktioniert nicht
            newOrder = CoffeeMachineOrder("", beverageID, timestamp)
            self._logOrder(newOrder)
            self._logStatus()
            return True
        else:
            return False

    def fillUpMilk(self):
        self.coffeeMachineStatus.remainingMilk = MAXMILK
        self._logStatus()
        return True

    def fillUpBeans(self):
        self.coffeeMachineStatus.remainingBeans = MAXBEANS
        self._logStatus()
        return True

    def fillUpWater(self):
        self.coffeeMachineStatus.remainingBeans = MAXWATER
        self._logStatus()
        return True

    def _checkRecommendationModule(self):
        #Is Recommendation Moduloe is active
        return True
    
    def _getScoredBeverageList(self):
        #Request an Recommendation Module
        results = []
        return results

    def _checkResources(self, id):
        return True #TODO Marek entfernen... Aktuell wird milch nicht wieder aufgefüllt, deshalb keine simulation durchführbar
        #if required resources > current resources --> True else False
        #if less than 10% of any resource is available --> call recommendation module
        enoughResourcesAvailable = True

        #Check if enough resources are available for the order
        if (
                self.coffeeMachineStatus.remainingBeans >= self._beverageDict.get(id).requiredBeans and
                self.coffeeMachineStatus.remainingMilk >= self._beverageDict.get(id).requiredMilk and
                self.coffeeMachineStatus.remainingWater >= self._beverageDict.get(id).requiredWater
        ):
            enoughResourcesAvailable = True
        else:
            enoughResourcesAvailable = False

        #Check available Resources and inform recommendation module if necessary
        if self.coffeeMachineStatus.remainingBeans < MAXBEANS * 0.1:
            #Call recommendation module
            #TODO
            pass

        if self.coffeeMachineStatus.remainingMilk < MAXMILK * 0.1:
            # Call recommendation module
            # TODO#
            pass

        if self.coffeeMachineStatus.remainingWater < MAXWATER * 0.1:
            # Call recommendation module
            # TODO#
            pass

        return enoughResourcesAvailable

    def _recalculateResources(self, id, timestamp):
        #Subtract required resources from current resources
        self.coffeeMachineStatus.powerOn = 1
        self.coffeeMachineStatus.energySaver = 0
        self.coffeeMachineStatus.timestamp = timestamp
        self.coffeeMachineStatus.grinderRuntime += self._beverageDict.get(id).grinderRuntime
        self.coffeeMachineStatus.id = ""
        self.coffeeMachineStatus.pumpRuntime += self._beverageDict.get(id).pumpRuntime
        self.coffeeMachineStatus.remainingBeans -= self._beverageDict.get(id).requiredBeans
        self.coffeeMachineStatus.remainingMilk -= self._beverageDict.get(id).requiredMilk
        self.coffeeMachineStatus.remainingWater -= self._beverageDict.get(id).requiredWater
        self.coffeeMachineStatus.machineRuntime += 30

    def _logOrder(self, newOrder):
        #Call DB module and log order
        addOrderEntry(newOrder)

    def _logStatus(self):
        #Call DB module and log order
        addStatusEntry(self.coffeeMachineStatus)
