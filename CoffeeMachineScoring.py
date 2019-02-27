from math import *
from BeverageList import getBeverageList
from DataController import getStatusEntries, getOrderEntries
from datetime import datetime



class CoffeeMachineScoring(object): 

	def __init__(self):
		self.ScoringList = {}


	#aufruf bei Scoring jedes Mal
	def perishablemilk(date):
		a = 6
		#a ist x Wert.
		#Wird von Milchstand geliefert und gibt den Prozentsatz des Füllstands wieder (0-10)
		y = 12.16*0.84**a
		#exponential Funktion f(x)=0.18 * 1.5**x
		liste = getBeverageList()
		#kann die getBeverageList nicht importieren FEHLER!!!!
		return (liste)
		day = date.weekday()
			
			
		return(int(y))

		#wird aufgerufen von CoffeeMachine 
	def daytime(date):
		hour = int(date.strftime("%H"))
		#liefert die aktuelle Stunde zurück
		if (hour > 5) & (hour < 13):
			prio = "morgens"
		elif (hour >= 13) & (hour < 18):
			prio = "mittags"
		else:
			prio = "abends"
		#Bestimmung der Zeitzone um daraus Prios zu setzen
		print (prio)
				

		
	#Funktion sortiert die Getränke nach Beliebtheit
	#muss in einem bestimmten Intervall aufgerufen werden durch CaffeeMachineObject
	def popularity():
	#leerer Zähler
		zaehler = [0,0,0,0,0,0]
	#Bestellungen werden per Funktionsaufrauf aus der Datenbank abgerufen
		pop = getOrderEntries()
	#leere Liste und leeres Dictionary werden erstellet
		dictonary = {}
	#die Anzahl der bestellten Getränke werden gezählt
		for i in pop:
			wert = zaehler [(i.beverageID)-1]
			zaehler [(i.beverageID)-1] = wert+1
	#Zahlenwert wird festgelegt
		drinkID = 1
	#Mittels der Schleife wird ein Dictionary erstellt Key=ID des Getränks, Value=Anzahl der Bestellungen
		for j in zaehler:
			zahl = drinkID-1
			dictonary[drinkID] = zaehler[zahl]
			drinkID += 1
	#Dictionary wird in Liste umgewandelt [(),(),...]
		bestellung = [(val,key)for key,val in dictonary.items()]
	#Dictionary wird nach Anzahl (Value) zunächst aufsteigend und anschließend absteigend sortiert	
		bestellung.sort()
		bestellung.reverse()
		beliebtheit = []
	#die IDs der Kaffees werden nach Beliebtheit in der Liste Beliebtheit eingeordnet	
		for k in bestellung:
			beliebtheit.append(k[1])
		return (beliebtheit)
		
	
	#muss automatisch ausgeführt werden
	def powersaver(date):
		hour = int(date.strftime("%H"))
		if(hour > 22) & (hour <5):
			return False
		else:
			return True

	
print(CoffeeMachineScoring.perishablemilk(datetime.now()))


