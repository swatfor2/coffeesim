class CoffeeMachineOrder:

    def __init__(self, id, beverageID, timestampOrder):
        self.id = id #Null Autoincrement from DB
        self.beverageID = beverageID  # int
        self.timestampOrder = timestampOrder  # String

    def toJSON(self):
        return {'id': self.id,
                              'beverageID': self.beverageID,
                           'timestampOrder': self.timestampOrder,
                           }