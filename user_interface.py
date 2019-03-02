from external import wasgibts
from random import randint
from CoffeeMachine import CoffeeMachine
from collections import OrderedDict
from operator import itemgetter  
from datetime import time

def next(timestamp):
    status, kaffeelist = wasgibts(timestamp)
    # print("Status -",status, "- Kaffeeliste - ",kaffeelist)
    coffeeMachine = CoffeeMachine();
    if(timecheck(timestamp)):
        for i in range(randint(1,5)):
            #orderlist = coffeeMachine.getBeverageList()
            orderlist = {'1': 1 , '2': 1, '3': 1, '4': 1, '5': 1, '6': 1}  #muss später durch die vorherige Zeile ersetzt werden, wir bekommen von der Maschine noch nichts
            #coffeeMachine.orderBeverage(choose(orderlist), timestamp) aktuell defekt      
    else:
        pass    

            coffeeMachine.orderBeverage(1,timestamp) #TODO 1 ersetzen

    random.seed()
    random_value = randint(0,1000) % len(modellist)
    
    returnlist = {}
    returnlist["1"] = modellist[random_value]["1"] * orderlist["1"]
    returnlist["2"] = modellist[random_value]["2"] * orderlist["2"]
    returnlist["3"] = modellist[random_value]["3"] * orderlist["3"]
    returnlist["4"] = modellist[random_value]["4"] * orderlist["4"]
    returnlist["5"] = modellist[random_value]["5"] * orderlist["5"]
    returnlist["6"] = modellist[random_value]["6"] * orderlist["6"]
    sortedList = OrderedDict(sorted(returnlist.items(), key = itemgetter(1), reverse = True))
    return(sortedList.popitem(last=False)[0])    
    
    
def timecheck(timestamp): 
    if(timestamp.hour < 18 and timestamp.hour > 7 and timestamp.isoweekday() < 6):
        return True
    else:
        return False
