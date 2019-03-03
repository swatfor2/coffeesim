"""Coffeemachine Simulation

This dashboard allows a simulation of a coffeemachine between 1 and 4 Weeks.

This script requires flask be installed within the Python
environment you are running this script in.

Author: Marcel Ament - marcel.ament@mercatis.com
"""

import os

from flask import Flask
from flask import render_template
from user_interface import Usermodel
from DataController import *
from datetime import datetime
from flask import request
from datetime import timedelta
import io
import csv
from flask import make_response

import time
import json

app = Flask(__name__)
userModel = Usermodel()


@app.route('/')
def renderTemplate():
        """Render the template

        Parameters
        ----------
        None

        Returns
        -------
        render_template
            a template with the orders and status in UTF 8
        """
        orders = getLastHundredOrderEntries();
        orderStr = json.dumps([e.toJSON() for e in getOrderEntries()])
        statusList = getLastHundredStatusEntries();
        return render_template('dashboard.html',orders=orders,orderStr=orderStr,statusList=statusList).encode("utf-8")


@app.route('/startSimulation')
def startSimulation():
        """Starts the simulation

        Parameters
        ----------
        Weeks
            Needs the number of weeks as args

        Returns
        -------
        String
            a string that will displayed if the simulation is finished
        """
        args = request.args
        wochen = args['wochen']
        #10080 Minuten pro woche
        minuten = 10080 * int(wochen)
        date = datetime.now();
        for x in range(minuten):
            date = date + timedelta(minutes = 1)
            userModel.interact(date)
        return "Simulation abgeschlossen"

@app.route('/deleteSimulation')
def deleteSimulationCall():
        """Delete the simulation

        Parameters
        ----------
        None

        Returns
        -------
        String
            a string that will displayed if the simulation is deleted
        """
        deleteSimulation()
        return "Alle Daten geloescht"

@app.route('/downloadOrders')
def downloadOrders():
    """Download the orders as CSV

        Parameters
        ----------
        None

        Returns
        -------
        String
            a commasperated string in a CSV format
    """
    si = io.StringIO()
    cw = csv.writer(si)
    csvData = [["ID","KaffeId","Datum und Uhrzeit"]];
    orders = getOrderEntries();
    for order in orders:
        orderToAdd = [order.id,order.beverageID,order.timestampOrder]
        csvData.append(orderToAdd)

    cw.writerows(csvData)
    output = make_response(si.getvalue())
    output.headers["Content-Disposition"] = "attachment; filename=Bestellungen.csv"
    output.headers["Content-type"] = "text/csv"
    return output

@app.route('/downloadStatus')
def downloadStatus():
    """Download the Status as CSV

        Parameters
        ----------
        None

        Returns
        -------
        String
            a commasperated string in a CSV format
        """
    si = io.StringIO()
    cw = csv.writer(si)
    csvData = [["ID","Datum und Uhrzeit","Anzeit","Stromsparmodus","Restliche Bohnen","Restliche Milch","Restliches Wasser","Laufzeit Pumpe", "Laufzeit Mühle", "Laufzeit Machine"]];
    status = getStatusEntries();
    for stat in status:
        statusToAdd = [stat.id,stat.timestamp,stat.powerOn,stat.energySaver,stat.remainingBeans,stat.remainingMilk,stat.remainingWater,stat.pumpRuntime,stat.grinderRuntime,stat.machineRuntime]
        csvData.append(statusToAdd)

    cw.writerows(csvData)
    output = make_response(si.getvalue())
    output.headers["Content-Disposition"] = "attachment; filename=Status.csv"
    output.headers["Content-type"] = "text/csv"
    return output

@app.route('/test')
def test():
    for x in range(10):
        userModel.interact(datetime.now())
    return "Überprüf das Log"

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port, debug=True)



