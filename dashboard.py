from flask import Flask
from flask import render_template
from user_interface import next
from DataController import getOrderEntries
from DataController import addOrderEntry
from CoffeeMachineOrder import CoffeeMachineOrder
from datetime import datetime

import time
import json

app = Flask(__name__)

@app.route('/')
def renderTemplate():
        orders = getOrderEntries();
        orderStr = json.dumps([e.toJSON() for e in orders])
        print(datetime.now());

        return render_template('dashboard.html',orders=orders,orderStr=orderStr).encode("utf-8")


@app.route('/startSimulation')
def startSimulation():
        next(datetime.now())
        return "Erfolgreich"

