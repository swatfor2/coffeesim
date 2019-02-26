from CoffeeMachineStatus import CoffeeMachineStatus
from CoffeeMachineOrder import CoffeeMachineOrder

import datetime


class CoffeeMachine(object):

    def __init__(self):
        self._standardBeverages = []
        self._scoredBeverages = []

        #List with required resources for products
        #[[1, "Cafè Créme", "200", "10", "0"], [...]] e.g. [[ID, Name, Required Water, Reqired Beans, Required Milk]]
        self._requiredResources = []
        self.coffeeMachineStatus = self._startUp()

    def _startUp(self):
        #check and get the States of the Machine
        #Request from DB
        #Filled with dummy data
        tempCoffeeMachineStatus = CoffeeMachineStatus(datetime.datetime.utcnow(), True, True, 10, 20, 150, 20, 3, 30)
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
        return False

    def _recalculateResources(self, id):
        #Subtract required resources from current resources
        pass

    def _logOrder(self, newOrder):
        #Call DB module and log order
        pass

    def _logStatus(self):
        #Call DB module and log order
        pass

    def _callDashboard(self, approved):
        pass
