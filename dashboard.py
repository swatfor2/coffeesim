from flask import Flask
from flask import render_template
from user_interface import next
from DataController import getEntries
import time

app = Flask(__name__)

@app.route('/')
def renderTemplate():
        return render_template('dashboard.html',orders=getEntries())


@app.route('/startSimulation')
def startSimulation():
        next(time.time())
        return "Erfolgreich"

