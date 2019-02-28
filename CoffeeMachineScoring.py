from math import *
from BeverageList import BeverageList
from BeverageList import BeverageItem
from DataController import getStatusEntries, getOrderEntries, getLatestStatus
from datetime import datetime

#beverageID, name, requiredBeans, requiredMilk, requiredWater, pumpRuntime, grinderRuntime
BeverageListe = [(1, "Café Crème", 5, 0, 150, 10, 5), (2, "Latte Machiatto", 4, 100, 100, 15, 4), (3, "Esprèsso", 5, 0, 25, 10, 5), (4, "Hot Water", 0, 0, 200, 15, 5), (5, "Milchkaffee", 5, 50, 150, 15, 5), (6, "Doppelter Esprèsso", 10, 0, 50, 20, 10)]

	

class CoffeeMachineScoring(object): 

	def __init__(self):
		self.ScoringList = {}

	#Funktion, die den Scouringwert berechnet
	def berechnungScore(date):
		scoringList = []
		for i in BeverageListe:
			scoringList.append([i[0], 0])
		#Tageszeit 
		#ScoringWert Wasser abrufen
		#ScoringWert Bohnen abrufen
		#ScoringWert Tageszeit abrufen
		CoffeeMachineScoring.daytime(scoringList,date)
		print("ScoringListe nach Tageszeit ")
		print(scoringList)
		#ScoringWert Wochentag abrufen
		#ScoringWert Beliebtheit abrufen
		CoffeeMachineScoring.popularity(scoringList)
		print("ScoringListe nach Beliebtheit ")
		print(scoringList)
		#ScoringWert Milch abrufen
		CoffeeMachineScoring.perishablemilk(scoringList)
		print("ScoringListe nach Milch")
		print(scoringList)
		#Scoring Bohnen abrufen
		CoffeeMachineScoring.perishablecoffee(scoringList)
		print("ScoringListe nach Kaffee")
		print(scoringList)
		#Scoring Wasser abrufen
		CoffeeMachineScoring.perishablewater(scoringList)
		print("ScoringListe nach Wasser")
		print(scoringList)



	#reduziert den Wert der Scoringliste prozentual, bemessen am Füllstand der Milch, sowie der benötigten Milchmenge pro Tasse. 
	def perishablemilk(scoringList):
		#rufe die Liste der Füllmengen aus der Datenbank ab. ########################################
		status = getLatestStatus()
		#a ist die Füllmenge (10 = 100%)
		a = status.remainingMilk
		a = a/10000
		#funktion zur Berechung des y-Werts der Funktion
		y = (12.16*(0.84**a)-2)*10
		#Schleife um jeweiliges Produkt aus der scoringList aufzurufen
		for sorte in scoringList:
			#zahl ist der Scoringwert der Kaffeesorte
			zahl = sorte[1]
			#if-Abfrage um nach MIlchprodukten zu filtern
			if (sorte[0] == 2):
				#Scoringwert wird reduziert
				sorte[1] = round((zahl-(zahl/100*y)))
			elif (sorte[0] == 5):
				#Scoringwert wird reduziert
				sorte[1] = round(zahl-(zahl/200*y))
			else:
				pass
		#Liefert neue Scoringliste zurück
		return(scoringList)
		
	#reduziert den Wert der Scoringliste prozentual, bemessen am Füllstand der Bohnen, sowie der benötigten Bohnenmenge pro Tasse. 
	def perishablecoffee(scoringList):
		#rufe die Liste der Füllmengen aus der Datenbank ab. ########################################
		status = getLatestStatus()
		#a ist die Füllmenge (10 = 100%)
		a = status.remainingBeans
		a = a/10
		#funktion zur Berechung des y-Werts der Funktion
		y = (-a+10)*10
		#Schleife um jeweiliges Produkt aus der scoringList aufzurufen
		for sorte in scoringList:
			#zahl ist der Scoringwert der Kaffeesorte
			zahl = sorte[1]
			#if-Abfrage um nach Kaffeemenge zu filtern
			if (sorte[0] == 6):
				#Scoringwert wird reduziert
				sorte[1] = round(zahl-(zahl/100*y))
			elif (sorte[0] == 1) or (sorte[0] == 3) or (sorte[0] == 5):
				#Scoringwert wird reduziert
				sorte[1] = round(zahl-(zahl/150*y))
			elif (sorte[0] == 2):
				#Scoringwert wird reduziert
				sorte[1] = round(zahl-(zahl/200*y))
			else:
				pass
		#Liefert neue Scoringliste zurück
		return(scoringList)
		
		
	#reduziert den Wert der Scoringliste prozentual, bemessen am Füllstand des Wassers, sowie der benötigten Wassermenge pro Tasse. 
	def perishablewater(scoringList):
		#rufe die Liste der Füllmengen aus der Datenbank ab. ########################################
		status = getLatestStatus()
		#a ist die Füllmenge (10 = 100%)
		a = status.remainingWater
		a = a/100
		#funktion zur Berechung des y-Werts der Funktion
		y = (-a+10)*10
		#Schleife um jeweiliges Produkt aus der scoringList aufzurufen
		for sorte in scoringList:
			#zahl ist der Scoringwert des Wassers
			zahl = sorte[1]
			#if-Abfrage um nach Wassermenge zu filtern
			if (sorte[0] == 4):
				#Scoringwert wird reduziert
				sorte[1] = round(zahl-(zahl/100*y))
			elif (sorte[0] == 1) or (sorte[0] == 5):
				#Scoringwert wird reduziert
				sorte[1] = round(zahl-(zahl/150*y))
			elif (sorte[0] == 2):
				#Scoringwert wird reduziert
				sorte[1] = round(zahl-(zahl/180*y))
			elif (sorte[0] == 6):
				#Scoringwert wird reduziert
				sorte[1] = round(zahl-(zahl/200*y))
			else:
				#Scoringwert wird reduziert
				sorte[1] = round(zahl-(zahl/220*y))
		#Liefert neue Scoringliste zurück
		return(scoringList)
	
	
	#Funktion zum Ermitteln und werten der typischen Beliebtheit von Produkten nach Tagezeiten
	def daytime(liste, date):
		#liefert die aktuelle Stunde zurück
		hour = int(date.strftime("%H"))
		#sortiert nach Tageszeit
		if (hour > 5) & (hour < 13):
			for element in liste:
				#Auswahl von Kaffee und Milchkaffe
				if (element[0]==1) or (element[0]==5):
					#Scoringwert steigt um 2
					element[1] +=2
		elif (hour >= 13) & (hour < 18):
			#Auswahl von Espresse
			for element in liste:
				if (element[0]==3) or (element[0]==6):
					#Scoringwert steigt um 2
					element[1] +=2
		else:
			for element in liste:
				#Auswahl von Latte und heißem Wasser
				if (element[0]==2) or (element[0]==4):
					#Scoringwert steigt um 2
					element[1] +=2
		#Bestimmung der Zeitzone um daraus Prios zu setzen
		return(liste)
				
		
	#Funktion sortiert die Getränke nach Beliebtheit
	def popularity(liste):
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

	#Rating wird in ScoringListe addiert
		zahl = 6
	# muss noch kommentiert werden ##########################################
		for element in beliebtheit:
			listenwert = element-1
			aktuellerScore = liste[listenwert][1]
			neuerScore = aktuellerScore + zahl
			liste[listenwert][1] = neuerScore
			zahl = zahl - 1
		return(liste)
                        
		
	
	#muss automatisch ausgeführt werden ##########################################
	def powersaver(date):
		hour = int(date.strftime("%H"))
		if(hour > 22) & (hour <5):
			return False
		else:
			return True


print(CoffeeMachineScoring.berechnungScore(datetime.now()))


