# =============================================================================
# Project: Simulation of a coffeemachine
# ClassName: Usermodel
# ClassPurpose: emulates a bunch of people with various coffee-prefers
# Inputs: Timestamp
# Outputs: Initiation of 0-3 ordererd coffees
# Author: WWI2016A - Max Hänsel, Patrick Heidel, Philipp Schmid, Florian Stoeber
# GitRepository: https://github.com/florianstoeber/coffeesim
# =============================================================================

import random
from random import randint
from coffee_machine_object import CoffeeMachine
from collections import OrderedDict
#from operator import itemgetter             #imported but unused 

class Usermodel(object):
    # =============================================================================
    # ClassName: Usermodel
    # ClassPurpose: emulates a bunch of people with various coffee-prefers
    # MethodeNames: interact, timecheck, chooseCoffee
    # CoffeeIds:
    #           1 - Cafe Creme
    #           2 - Latte Machiatto
    #           3 - Espresso
    #           4 - Hot Water (tea)
    #           5 - Milchkaffee
    #           6 - Doppelter Espresso
    # =============================================================================
    
    
    def __init__(self):
        # =============================================================================
        # MethodPurpose: Initiiation of the object and defining of various usermodels
        # Each usermodel prefers different types of coffee
        # if a type of coffee is preferred by a user the index is set with 100
        # the last three models only use the reccomendation of the machine
        # the usermodels are used in the chooseCoffee-method
        # =============================================================================
        
        self.modellist = [
           {'1': 0 , '2': 0, '3': 0, '4': 100, '5': 0, '6': 0},             #just tea
           {'1': 60 , '2': 0, '3': 70, '4': 15, '5': 0, '6': 80},           #only black coffee
           {'1': 0 , '2': 100, '3': 0, '4': 25, '5': 60, '6': 0},           #just white coffee with the pereferation of Latte Machiatto
           {'1': 50 , '2': 0, '3': 100, '4': 15, '5': 0, '6': 60},          #prefering espresso 
           {'1': 0 , '2': 60, '3': 0, '4': 25, '5': 100, '6': 0},           #just white coffee with the pereferation of Milchkaffee
           {'1': 50 , '2': 0, '3': 60, '4': 0, '5': 0, '6': 100},           #preferring double espresso
           {'1': 85 , '2': 60, '3': 0, '4': 30, '5': 85, '6': 0},           #no preferations
           {'1': 85 , '2': 85, '3': 0, '4': 30, '5': 60, '6': 0},           #no preferations 2
           {'1': 100 , '2': 100, '3': 100, '4': 100, '5': 100, '6': 100},   #using only the reccomendation
           {'1': 100 , '2': 0, '3': 100, '4': 0, '5': 0, '6': 100},         #using only the reccomendation wtihout milk
           {'1': 0 , '2': 100, '3': 0, '4': 100, '5': 100, '6': 0}          #using only the reccomendation but no balck coffee
           ]
        
        random.seed()
        self.coffeeMachine = CoffeeMachine()
        
    def interact(self, timestamp):
        # =============================================================================
        # MethodPurpose: Get the available coffees from the coffeemachine multiplies it with a ranodm user from the user-models. 
        # 0-3 coffees are ordered in one method-call
        # =============================================================================
        
        if(self.timecheck(timestamp)):
            for i in range(randint(0,3)):
                orderlist = self.coffeeMachine.getBeverageList(timestamp)
                self.coffeeMachine.orderBeverage(self.chooseCoffee(orderlist), timestamp)  
        else:
            pass   
        
    def timecheck(self, timestamp):
        # =============================================================================
        # MethodPurpose: Returns True if the datetime is beetween Monday and Friday and between 8 and 18 o clock; otherwise it returns a negative boolean       
        # =============================================================================
        if(timestamp.hour < 18 and timestamp.hour > 7 and timestamp.isoweekday() < 6):
            return True
        else:
            return False

    def chooseCoffee(self, orderlist):
        # =============================================================================
        # MethodPurpose: Returns the most preferred coffee-id
        # Descirption: Multiplies the available coffeelist with one model that is choosed randomly
        # =============================================================================
        random_value = randint(0,1000) % len(self.modellist)
        returnlist = {}
        returnlist["1"] = self.modellist[random_value]["1"] * orderlist["1"]["score"]
        returnlist["2"] = self.modellist[random_value]["2"] * orderlist["2"]["score"]
        returnlist["3"] = self.modellist[random_value]["3"] * orderlist["3"]["score"]
        returnlist["4"] = self.modellist[random_value]["4"] * orderlist["4"]["score"]
        returnlist["5"] = self.modellist[random_value]["5"] * orderlist["5"]["score"]
        returnlist["6"] = self.modellist[random_value]["6"] * orderlist["6"]["score"]
        sortedList = OrderedDict(sorted(returnlist.items(), key=lambda x: -x[1]))
        return(sortedList.popitem(last=False)[0])
