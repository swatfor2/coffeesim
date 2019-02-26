from random import randint


def wasgibts(timestamp):
    random_wert = randint(0, 100)
    if random_wert < 100:
        status = True
        # kaffee = ["espresso", "cafe crema", "latte macchiato", "milch"]
        kaffeelist = [{
            "name": "espresso",
            "score": randint(0, 10) * 100,
        }, {
            "name":  "cafe crema",
            "score": randint(0, 10) * 100,
        }, {
            "name":  "latte macchiato",
            "score": randint(0, 10) * 100,
        }, {
            "name": "milch",
            "score": randint(0, 10) * 100,
        }]
        return status, kaffeelist
    else:
        status = False
        kaffeelist = {}
        return status, kaffeelist


def order(timestap, order):
    return order, "einmal bestellt"
