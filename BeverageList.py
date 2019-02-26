class BeverageList(object):

    def __init__(self):
        self.beverageList = []
        #beverageID, name, requiredBeans, requiredMilk, requiredWater, pumpRuntime, grinderRuntime
        self.beverageList.append(BeverageItem(1, "Café Crème", 5, 0, 150, 10, 5))
        self.beverageList.append(BeverageItem(2, "Latte Machiatto", 4, 100, 100, 15, 4))
        self.beverageList.append(BeverageItem(3, "Esprèsso", 5, 0, 25, 10, 5))
        self.beverageList.append(BeverageItem(4, "Hot Water", 0, 0, 200, 15, 5))
        self.beverageList.append(BeverageItem(5, "Milchkaffee", 5, 50, 150, 15, 5))
        self.beverageList.append(BeverageItem(6, "Doppelter Esprèsso", 10, 0, 50, 20, 10))

    def getBeverageList(self):
        return self.beverageList


class BeverageItem(object):

    def __init__(self, beverageID, name, remainingBeans, remainingMilk, remainingWater, pumpRuntime, grinderRuntime):
        self.beverageID = beverageID
        self.name = name
        self.score = 0
        self.remainingBeans = remainingBeans
        self.remainingMilk = remainingMilk
        self.remainingWater = remainingWater
        self.pumpRuntime = pumpRuntime
        self.grinderRuntime = grinderRuntime

