import sqlite3
from CoffeeMachineOrder import CoffeMachineOrder



def getEntries():
    conn = sqlite3.connect('CoffeeMachineDB.db')
    c = conn.cursor()
    c.execute("SELECT * FROM ORDERS")
    rows = c.fetchall()
    orders = []
    for row in rows:
        orders.append(CoffeMachineOrder(row[0],row[1],row[2]))
    return orders



def addEntry(order):
    conn = sqlite3.connect('CoffeeMachineDB.db')
    c = conn.cursor()
    c.execute('insert into ORDERS (beverageUUID,timestampOrder) values ({0},{1})'.format(order.beverageUUID,order.timestampOrder))
    conn.commit()


order = CoffeMachineOrder("", 2, "25")
addEntry(order)