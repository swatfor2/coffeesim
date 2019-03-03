class BeverageList(object):

    def __init__(self):
        self.beverageList = []
        self.beverageDict = {}
        #beverageID, name, requiredBeans, requiredMilk, requiredWater, pumpRuntime, grinderRuntime
        self.beverageList.append(BeverageItem(1, "Café Crème", 5, 0, 150, 10, 5))
        self.beverageList.append(BeverageItem(2, "Latte Machiatto", 4, 100, 100, 15, 4))
        self.beverageList.append(BeverageItem(3, "Esprèsso", 5, 0, 25, 10, 5))
        self.beverageList.append(BeverageItem(4, "Hot Water", 0, 0, 200, 15, 5))
        self.beverageList.append(BeverageItem(5, "Milchkaffee", 5, 50, 150, 15, 5))
        self.beverageList.append(BeverageItem(6, "Doppelter Esprèsso", 10, 0, 50, 20, 10))

        self.beverageDict['1'] = {"item":BeverageItem(1, "Café Crème", 5, 0, 150, 10, 5), "score": 0.5}
        self.beverageDict['2'] = {"item":BeverageItem(2, "Latte Machiatto", 4, 100, 100, 15, 4), "score":0.1}
        self.beverageDict['3'] = {"item":BeverageItem(3, "Esprèsso", 5, 0, 25, 10, 5), "score":0.1}
        self.beverageDict['4'] = {"item":BeverageItem(4, "Hot Water", 0, 0, 200, 15, 5), "score":0.1}
        self.beverageDict['5'] = {"item":BeverageItem(5, "Milchkaffee", 5, 50, 150, 15, 5), "score":0.1}
        self.beverageDict['6'] = {"item":BeverageItem(6, "Doppelter Esprèsso", 10, 0, 50, 20, 10), "score":0.1}

    def getBeverageList(self):
        return self.beverageList

    def getBeverageDict(self):
        return self.beverageDict


class BeverageItem(object):

    def __init__(self, beverageID, name, requiredBeans, requiredMilk, requiredWater, pumpRuntime, grinderRuntime):
        self.beverageID = beverageID
        self.name = name
        self.score = 0
        self.requiredBeans = requiredBeans
        self.requiredMilk = requiredMilk
        self.requiredWater = requiredWater
        self.pumpRuntime = pumpRuntime
        self.grinderRuntime = grinderRuntime

