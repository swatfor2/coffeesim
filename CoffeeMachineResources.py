class CoffeeMachineResources(object):

    def __init__(self):
        self.resourcesList = []
        #resourceID, name, amount
        self.resourcesList.append(1, "Water", 100)
        self.resourcesList.append(2, "Beans", 100)
        self.resourcesList.append(3, "Milk", 100)
        #self.beverageList.append(BeverageItem(4, "Power", 100))

#selbes Problem wie in der anderen Datei. Ich bekomme die Liste nicht returned.... 
    def getResources(self):
        return self.resourcesList
		
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
		
print(CoffeeMachineResources.getResources())