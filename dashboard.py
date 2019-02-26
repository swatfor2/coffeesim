from flask import Flask
from flask import render_template
from user_interface import next
from DataController import getEntries
from DataController import addEntry
from CoffeeMachineOrder import CoffeMachineOrder

import time
import json

app = Flask(__name__)

@app.route('/')
def renderTemplate():
        orders = getEntries();
        orderStr = json.dumps([e.toJSON() for e in orders])
        print(orderStr);

        return render_template('dashboard.html',orders=getEntries(),orderStr=orderStr).encode("utf-8")


@app.route('/startSimulation')
def startSimulation():
        next(time.time())
        return "Erfolgreich"

