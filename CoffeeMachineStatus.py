class CoffeeMachineStatus(object):
    def __init__(self, timestamp, powerOn, energySaver, requiredBeans, requiredMilk, requiredWater, pumpRuntime, grinderRuntime, machineRuntime):
        self.timestamp = timestamp #String
        self.powerOn = powerOn #bool
        self.energySaver = energySaver #bool
        self.requiredBeans = requiredBeans
        self.requiredMilk = requiredMilk
        self.requiredWater = requiredWater
        self.pumpRuntime = pumpRuntime
        self.grinderRuntime = grinderRuntime
        self.machineRuntime = machineRuntime

    def __str__(self):
        return self.powerOn
