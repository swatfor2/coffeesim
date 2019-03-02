from external import wasgibts
from random import randint
from CoffeeMachine import *

def next(timestamp):
    status, kaffeelist = wasgibts(timestamp)
    # print("Status -",status, "- Kaffeeliste - ",kaffeelist)
    coffeeMachine = CoffeeMachine();
    if status is True:
        random_wert_recommendation = randint(0, 100)
        if random_wert_recommendation > randint(0, 50):
            print("recommendation benutzt")
            sorted_kaffeelist = sorted(
                kaffeelist, key=lambda k: k['score'], reverse=True)

            coffeeMachine.orderBeverage(1,timestamp) #TODO 1 ersetzen

        else:
            print("recommendation nicht benutzt")
            coffeeMachine.orderBeverage(1,timestamp) #TODO 1 ersetzen
    elif status is False:
        print("Kaffemaschine nicht erreichbar")
        pass
    else:
        pass


