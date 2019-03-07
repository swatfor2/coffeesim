class CoffeeMachineStatus(object):
    def __init__(self, id, timestamp, powerOn, energySaver, remainingBeans, remainingMilk, remainingWater, pumpRuntime, grinderRuntime, machineRuntime):
        self.id = id
        self.timestamp = timestamp #String
        self.powerOn = powerOn #bool
        self.energySaver = energySaver #bool
        self.remainingBeans = remainingBeans #remainingBeans Gramm
        self.remainingMilk = remainingMilk #remainingMilk ml
        self.remainingWater = remainingWater #remainingWater ml
        self.pumpRuntime = pumpRuntime #Seconds
        self.grinderRuntime = grinderRuntime #Seconds
        self.machineRuntime = machineRuntime #Seconds

    def __str__(self):
        return self.powerOn

    def copy(self):
        newone = type(self)(self.id, self.timestamp, self.powerOn, self.energySaver, self.remainingWater, self.remainingBeans, self.remainingMilk, self.pumpRuntime, self.grinderRuntime, self.machineRuntime)
        newone.__dict__.update(self.__dict__)
        return newone
