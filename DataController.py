import sqlite3
from CoffeeMachineOrder import CoffeeMachineOrder
from CoffeeMachineStatus import CoffeeMachineStatus




def getOrderEntries():
    conn = sqlite3.connect('CoffeeMachineDB.db')
    c = conn.cursor()
    c.execute("SELECT * FROM ORDERS")
    rows = c.fetchall()
    orders = []
    for row in rows:
        orders.append(CoffeeMachineOrder(row[0],row[1],row[2]))
    return orders



def addOrderEntry(order):
    conn = sqlite3.connect('CoffeeMachineDB.db')
    c = conn.cursor()
    print('insert into ORDERS (beverageUUID,timestampOrder) values ({0},"{1}")'.format(order.beverageID,order.timestampOrder))
    c.execute('insert into ORDERS (beverageUUID,timestampOrder) values ({0},"{1}")'.format(order.beverageID,order.timestampOrder))
    conn.commit()



def getStatusEntries():
    conn = sqlite3.connect('CoffeeMachineDB.db')
    c = conn.cursor()
    c.execute("SELECT * FROM STATUS")
    rows = c.fetchall()
    statusList = []
    for row in rows:
        statusList.append(CoffeeMachineStatus(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]))
    return statusList


def getLatestStatus():
    conn = sqlite3.connect('CoffeeMachineDB.db')
    c = conn.cursor()
    c.execute("SELECT * FROM STATUS WHERE id = (SELECT MAX(id) FROM STATUS)")
    rows = c.fetchall()
    statusList = []
    for row in rows:
        statusList.append(CoffeeMachineStatus(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]))
    return statusList[0]


def addStatusEntry(status):
    conn = sqlite3.connect('CoffeeMachineDB.db')
    c = conn.cursor()
    c.execute('insert into STATUS (timestamp,powerOn,energySaver,remainingBeans,remainingMilk,remainingWater,pumpRuntime,grinderRuntime,machineRuntime) values ("{0}","{1}","{2}","{3}","{4}","{5}","{6}","{7}","{8}")'.format(status.timestamp,status.powerOn,status.energySaver,status.remainingBeans,status.remainingMilk,status.remainingWater,status.pumpRuntime,status.grinderRuntime,status.machineRuntime))
    conn.commit()


def deleteSimulation():
    print("delete")
    conn = sqlite3.connect('CoffeeMachineDB.db')
    c = conn.cursor()
    c.execute("DELETE FROM STATUS")
    c.execute("DELETE FROM ORDERS")
    conn.commit()



