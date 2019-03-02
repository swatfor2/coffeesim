import random
from external import wasgibts
from random import randint
from CoffeeMachine import CoffeeMachine
from collections import OrderedDict
from operator import itemgetter   

#def next(timestamp):
#    status, kaffeelist = wasgibts(timestamp)
#    #print("Status -",status, "- Kaffeeliste - ",kaffeelist)
#    coffeeMachine = CoffeeMachine();
#    if status is True:
#        random_wert_recommendation = randint(0, 100)
#        if random_wert_recommendation > randint(0, 50):
#            print("recommendation benutzt")
#            sorted_kaffeelist = sorted(
#                kaffeelist, key=lambda k: k['score'], reverse=True)
#
#            coffeeMachine.orderBeverage(1,timestamp) #TODO 1 ersetzen
#
#        else:
#            print("recommendation nicht benutzt")
#            coffeeMachine.orderBeverage(1,timestamp) #TODO 1 ersetzen
#    elif status is False:
#        print("Kaffemaschine nicht erreichbar")
#        pass
#    else:
#        pass

def next(timestamp):
    coffeeMachine = CoffeeMachine();
    orderlist = coffeeMachine.getBeverageList()
    coffeeMachine.orderBeverage(choose(orderlist), timestamp)
    
    

def choose(orderlist):
    
#orderlist --> 1 Cafe Creme; 2 Latte Machiatto; 3 Espresso; 4 Hot Water; 5 Milchkaffe; 6 Doppelter Espresso;
     
    modellist = [
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
    random_value = randint(0,1000) % modellist.Length()
    
    returnlist = {}
    returnlist["1"] = modellist[random_value]["1"] * orderlist["1"]
    returnlist["2"] = modellist[random_value]["2"] * orderlist["2"]
    returnlist["3"] = modellist[random_value]["3"] * orderlist["3"]
    returnlist["4"] = modellist[random_value]["4"] * orderlist["4"]
    returnlist["5"] = modellist[random_value]["5"] * orderlist["5"]
    returnlist["6"] = modellist[random_value]["6"] * orderlist["6"]
    sortedList = OrderedDict(sorted(returnlist.items(), key = itemgetter(1), reverse = True))
    return(sortedList.popitem(last=False)[0])
        
    

    
    