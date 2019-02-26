class CoffeMachineOrder:

    def __init__(self, id, beverageUUID, timestampOrder):
        self.id = id #Null Autoincrement from DB
        self.beverageUUID = beverageUUID  # int
        self.timestampOrder = timestampOrder  # String