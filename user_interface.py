from external import wasgibts
from external import order
from random import randint


def next(timestamp):
    status, kaffeelist = wasgibts(timestamp)
    # print("Status -",status, "- Kaffeeliste - ",kaffeelist)
    if status is True:
        random_wert_recommendation = randint(0, 100)
        if random_wert_recommendation > randint(0, 50):
            print("recommendation benutzt")
            sorted_kaffeelist = sorted(
                kaffeelist, key=lambda k: k['score'], reverse=True)
            order_user = order(timestamp, sorted_kaffeelist[0]["name"])
            print(order_user)
        else:
            print("recommendation nicht benutzt")
            order_user = order(
                timestamp, kaffeelist[randint(0, len(kaffeelist)-1)]["name"])
    elif status is False:
        print("Kaffemaschine nicht erreichbar")
        pass
    else:
        pass


