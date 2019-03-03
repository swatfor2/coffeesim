import sqlite3

from coffee_machine_object import status
from coffee_machine_object import order
from coffee_machine_object import constants


def getOrderEntries():
    conn = sqlite3.connect('CoffeeMachineDB.db')
    c = conn.cursor()
    c.execute("SELECT * FROM ORDERS")
    rows = c.fetchall()
    orders = []
    for row in rows:
        orders.append(order.CoffeeMachineOrder(row[0],row[1],row[2]))
    return orders

def getLastHundredOrderEntries():
    conn = sqlite3.connect('CoffeeMachineDB.db')
    c = conn.cursor()
    c.execute("SELECT * FROM ORDERS ORDER BY ID DESC LIMIT 100")
    rows = c.fetchall()
    orders = []
    for row in rows:
        orders.append(order.CoffeeMachineOrder(row[0],row[1],row[2]))
    return orders




def addOrderEntry(order):
    conn = sqlite3.connect('CoffeeMachineDB.db')
    c = conn.cursor()
    c.execute('insert into ORDERS (beverageUUID,timestampOrder) values ({0},"{1}")'.format(order.beverageID,order.timestampOrder))
    conn.commit()



def getStatusEntries():
    conn = sqlite3.connect('CoffeeMachineDB.db')
    c = conn.cursor()
    c.execute("SELECT * FROM STATUS")
    rows = c.fetchall()
    statusList = []
    for row in rows:
        statusList.append(status.CoffeeMachineStatus(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]))
    return statusList

def getLastHundredStatusEntries():
    conn = sqlite3.connect('CoffeeMachineDB.db')
    c = conn.cursor()
    c.execute("SELECT * FROM STATUS ORDER BY ID DESC LIMIT 100")
    rows = c.fetchall()
    statusList = []
    for row in rows:
        statusList.append(status.CoffeeMachineStatus(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]))
    return statusList


def getLatestStatus():
    conn = sqlite3.connect('CoffeeMachineDB.db')
    c = conn.cursor()
    c.execute("SELECT * FROM STATUS WHERE id = (SELECT MAX(id) FROM STATUS)")
    row = c.fetchone()
    if row is None:
        #Check if DB is Empty
        return status.CoffeeMachineStatus("", "", 1, 0, constants.MAXBEANS, constants.MAXMILK, constants.MAXWATER, 0, 0, 0)
    else:
        return status.CoffeeMachineStatus(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9])




def addStatusEntry(status):
    conn = sqlite3.connect('CoffeeMachineDB.db')
    c = conn.cursor()
    c.execute('insert into STATUS (timestamp,powerOn,energySaver,remainingBeans,remainingMilk,remainingWater,pumpRuntime,grinderRuntime,machineRuntime) values ("{0}","{1}","{2}","{3}","{4}","{5}","{6}","{7}","{8}")'.format(status.timestamp,status.powerOn,status.energySaver,status.remainingBeans,status.remainingMilk,status.remainingWater,status.pumpRuntime,status.grinderRuntime,status.machineRuntime))
    conn.commit()


def deleteSimulation():
    conn = sqlite3.connect('CoffeeMachineDB.db')
    c = conn.cursor()
    c.execute("DELETE FROM STATUS")
    c.execute("DELETE FROM ORDERS")
    conn.commit()
