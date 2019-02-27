import os

from flask import Flask
from flask import render_template
from user_interface import next
from DataController import getOrderEntries
from DataController import getStatusEntries
from DataController import deleteSimulation
from datetime import datetime
from flask import request
from datetime import timedelta

import time
import json

app = Flask(__name__)

@app.route('/')
def renderTemplate():
        orders = getOrderEntries();
        orderStr = json.dumps([e.toJSON() for e in orders])
        statusList = getStatusEntries();
        return render_template('dashboard.html',orders=orders,orderStr=orderStr,statusList=statusList).encode("utf-8")


@app.route('/startSimulation')
def startSimulation():
        args = request.args
        wochen = args['wochen']
        #10080 Minuten pro woche
        minuten = 10080 * int(wochen)
        date = datetime.now();
        for x in range(minuten):
            date = date + timedelta(minutes = 1)
            next(date)

        return "Simulation abgeschlossen"

@app.route('/deleteSimulation')
def deleteSimulationCall():
        deleteSimulation()
        return "Alle Daten geloescht"


if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port, debug=True)