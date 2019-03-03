import random
from random import randint
from CoffeeMachine import CoffeeMachine
from collections import OrderedDict
from operator import itemgetter  

class Usermodel(object):
    def __init__(self):
        #orderlist --> 1 Cafe Creme; 2 Latte Machiatto; 3 Espresso; 4 Hot Water; 5 Milchkaffe; 6 Doppelter Espresso;
        self.modellist = [
           {'1': 0 , '2': 0, '3': 0, '4': 100, '5': 0, '6': 0},            #nur Tee
           {'1': 100 , '2': 0, '3': 70, '4': 15, '5': 0, '6': 25},         #nur Schwarz
           {'1': 0 , '2': 100, '3': 0, '4': 25, '5': 60, '6': 0},          #nur Weiß aber eher Latte Machiatto
           {'1': 25 , '2': 0, '3': 70, '4': 15, '5': 0, '6': 100},         #Esspressobevorzugende
           {'1': 0 , '2': 60, '3': 0, '4': 25, '5': 100, '6': 0},          #nur Weiß aber eher Milchkaffee
           {'1': 80 , '2': 30, '3': 0, '4': 70, '5': 70, '6': 0},          #Der Allrounder
           {'1': 70 , '2': 70, '3': 0, '4': 80, '5': 30, '6': 0},          #Der Allrounder II
           {'1': 100 , '2': 100, '3': 100, '4': 100, '5': 100, '6': 100},  #Reccommendation
           {'1': 100 , '2': 0, '3': 100, '4': 0, '5': 0, '6': 100},        #Reccommendation ohne Milch
           {'1': 0 , '2': 100, '3': 0, '4': 100, '5': 100, '6': 0}         #Reccommendation nur Milch und Tee
           ]
        random.seed()
        
    def interact(self, timestamp):
        coffeeMachine = CoffeeMachine()
        if(self.timecheck(timestamp)):
            for i in range(randint(0,3)):
                #orderlist = coffeeMachine.getBeverageList()
                orderlist = {'1': 1 , '2': 1, '3': 1, '4': 1, '5': 1, '6': 1}  #muss später durch die vorherige Zeile ersetzt werden, wir bekommen von der Maschine noch nichts
                coffeeMachine.orderBeverage(self.chooseCoffee(orderlist), timestamp)
                print(self.chooseCoffee(orderlist))
        else:
            pass   
        
    def timecheck(self, timestamp):
        if(timestamp.hour < 18 and timestamp.hour > 7 and timestamp.isoweekday() < 6):
            return True
        else:
            return False

    def chooseCoffee(self, orderlist):
        random_value = randint(0,1000) % len(self.modellist)
        returnlist = {}
        returnlist["1"] = self.modellist[random_value]["1"] * orderlist["1"]
        returnlist["2"] = self.modellist[random_value]["2"] * orderlist["2"]
        returnlist["3"] = self.modellist[random_value]["3"] * orderlist["3"]
        returnlist["4"] = self.modellist[random_value]["4"] * orderlist["4"]
        returnlist["5"] = self.modellist[random_value]["5"] * orderlist["5"]
        returnlist["6"] = self.modellist[random_value]["6"] * orderlist["6"]
        sortedList = OrderedDict(sorted(returnlist.items(), key = itemgetter(1), reverse = True))
        return(sortedList.popitem(last=False)[0])
        
    

    
