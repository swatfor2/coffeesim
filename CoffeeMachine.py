from CoffeeMachineStatus import CoffeeMachineStatus
from CoffeeMachineOrder import CoffeeMachineOrder
from DataController import addOrderEntry, getOrderEntries, getLatestStatus, addStatusEntry
from BeverageList import BeverageList, BeverageItem

import datetime


class CoffeeMachine(object):

    def __init__(self):
        self.beverageList = BeverageList()
        self._standardBeverages = self.beverageList.getBeverageList()
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
            self._recalculateResources(beverageID)
            newOrder = CoffeeMachineOrder("", beverageID, timestamp)
            self._logOrder(newOrder)
            #recalculate status
            self.coffeeMachineStatus.powerOn = 1
            self.coffeeMachineStatus.energySaver = 0
            self.coffeeMachineStatus.timestamp = timestamp
            self.coffeeMachineStatus.grinderRuntime += self._standardBeverages[beverageID + 1].grinderRuntime
            self.coffeeMachineStatus.id = ""
            self.coffeeMachineStatus.pumpRuntime += self._standardBeverages[beverageID + 1].pumpRuntime
            self.coffeeMachineStatus.requiredBeans -= self._standardBeverages[beverageID + 1].requiredBeans
            self.coffeeMachineStatus.requiredMilk -= self._standardBeverages[beverageID + 1].requiredMilk
            self.coffeeMachineStatus.requiredWater -= self._standardBeverages[beverageID + 1].requiredWater
            self._logStatus()
            self._callDashboard(True)
            return True
        else:
            self._callDashboard(False)
            return False

    def _checkRecommendationModule(self):
        #Is Recommendation Moduloe is active
        return True
    
    def _getScoredBeverageList(self):
        #Request an Recommendation Module
        results = []
        return results

    def _checkResources(self, id):
        #if required resources > current resources --> True else False
        #get Statusobject from DB
        return True

    def _recalculateResources(self, id):
        #Subtract required resources from current resources
        pass

    def _logOrder(self, newOrder):
        #Call DB module and log order
        addOrderEntry(newOrder)

    def _logStatus(self):
        #Call DB module and log order
        addStatusEntry(self.coffeeMachineStatus)

    def _callDashboard(self, approved):
        pass
