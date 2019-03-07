# =============================================================================
# Project: Simulation einer Kaffeemaschine
# ClassName: Empfehlungsmodul mit Randbedingungen
# ClassPurpose: 1) Erstellt eine Scoringliste, um das Benutzerverhalten zu beeinflussen.
#               2) Rahmenbedingungen erstellen, um die Situation realistischer zu gestallten. 
# Inputs: Timestamp
# Outputs: Scoringlist und Rehmenbedingungen 
# Author: WWI2016A - Anna Zaczek, Silja Barth, Kerstin Hofelich, Tim Decker-Conradi
# GitRepository: https://github.com/florianstoeber/coffeesim
# =============================================================================

from math import *
from DataController import getStatusEntries, getOrderEntries, getLatestStatus
from datetime import datetime
from coffee_machine_object import constants

# =====================================================================================
# GlobalList: BeverageListe
# CoffeeIds:
#           1 - Cafe Creme
#           2 - Latte Machiatto
#           3 - Espresso
#           4 - Hot Water (tea)
#           5 - Milchkaffee
#           6 - Doppelter Espresso
# ListPostions: 
#           1 - beverageID
#           2 - name
#           3 - requireBeans
#           4 - requiredMilk
#           5 - requiredWater
#           6 - pumpRuntime
#           7 - grinderRuntime
# =====================================================================================
BeverageListe = [(1, "Café Crème", 5, 0, 150, 10, 5), (2, "Latte Machiatto", 4, 100, 100, 15, 4), (3, "Esprèsso", 5, 0, 25, 10, 5), (4, "Hot Water", 0, 0, 200, 15, 5), (5, "Milchkaffee", 5, 50, 150, 15, 5), (6, "Doppelter Esprèsso", 10, 0, 50, 20, 10)]

	

class CoffeeMachineScoring(object): 
# =====================================================================================
# ClassName: CoffeeMachineScoring
# ClassPurpose: erstellen einer Scoringliste
# MethodeNames: berechnungScore, perishablemilk, perishablecoffee, perishablewater, daytime, popularity, powersaver, decision
# =====================================================================================

	def __init__(self):
		self.ScoringList = {}
        # =============================================================================
        # MethodPurpose: Initiierung des Objekts
        # =============================================================================
	
	#Funktion, die den Scouringwert berechnet
	def berechnungScore(date, status, bestellliste):
		# =====================================================================
        	# MethodPurpose: Berechnung der Scoringwerts jeder Kaffeesorte
		# Input: Timestamp, Füllmengen, Anzahl der bestellten Getränke
		# Output: Scouringliste
        	# =====================================================================
		scoringList = []
		for i in BeverageListe:
			scoringList.append([i[0], 0]					# ScoringWert Tageszeit abrufen
		CoffeeMachineScoring.daytime(scoringList,date)				# ScoringWert Beliebtheit abrufen
		CoffeeMachineScoring.popularity(scoringList, bestellliste)		# ScoringWert Milch abrufen
		CoffeeMachineScoring.perishablemilk(scoringList, status)		# Scoring Bohnen abrufen
		CoffeeMachineScoring.perishablecoffee(scoringList, status)		# Scoring Wasser abrufen
		CoffeeMachineScoring.perishablewater(scoringList, status)
		return(scoringList)

	def perishablemilk(scoringList, status):
		# =====================================================================
        	# MethodPurpose: reduziert den Wert der Scoringliste prozentual, bemessen am Füllstand der Milch, sowie der benötigten Milchmenge pro Tasse. 
		# Input: Scoringlist, Füllmengen
		# Output: neue Scouringliste
        	# =====================================================================
		a = status.remainingMilk						# rufe die Liste der Füllmengen (10 = 100%)
		a = a/constants.MAXMILK
		y = (12.16*(0.84**a)-2)*10						# Funktion zur Bestimmung des negativen Scoringwerts
		for sorte in scoringList:						# Aufruf der Scoringliste
			zahl = sorte[1]
			if (sorte[0] == 2):						# Abfrage nach Milchprodukten
				sorte[1] = round((zahl-(zahl/100*y)))			# Scoringwert wird reduziert
			elif (sorte[0] == 5):
				sorte[1] = round(zahl-(zahl/200*y))			# Scoringwert wird reduziert
			else:
				pass
		return(scoringList)
		 
	def perishablecoffee(scoringList, status):
		# =====================================================================
        	# MethodPurpose: reduziert den Wert der Scoringliste prozentual, bemessen am Füllstand der Bohnen, sowie der benötigten Bohnenmenge pro Tasse. 
		# Input: Scoringlist, Füllmengen
		# Output: neue Scouringliste
        	# =====================================================================
		a = status.remainingBeans						# rufe die Liste der Füllmengen (10 = 100%)
		a = a/constants.MAXBEANS
		y = (-a+10)*10								# Funktion zur Bestimmung des negativen Scoringwerts
		for sorte in scoringList:						# Aufruf der Scoringliste
			zahl = sorte[1]
			if (sorte[0] == 6):						# Abfrage nach Kaffeemengen
				sorte[1] = round(zahl-(zahl/100*y))			# Scoringwert wird reduziert
			elif (sorte[0] == 1) or (sorte[0] == 3) or (sorte[0] == 5):	# Scoringwert wird reduziert
				sorte[1] = round(zahl-(zahl/150*y))
			elif (sorte[0] == 2):
				sorte[1] = round(zahl-(zahl/200*y))			# Scoringwert wird reduziert
			else:
				pass
		return(scoringList)
		
	def perishablewater(scoringList, status):
		# =====================================================================
        	# MethodPurpose: reduziert den Wert der Scoringliste prozentual, bemessen am Füllstand des Wassers, sowie der benötigten Wassermenge pro Tasse.  
		# Input: Scoringlist, Füllmengen
		# Output: neue Scouringliste
        	# =====================================================================
		a = status.remainingWater						# rufe die Liste der Füllmengen (10 = 100%)
		a = a/constants.MAXWATER
		y = (-a+10)*10								# Funktion zur Bestimmung des negativen Scoringwerts
		for sorte in scoringList:						# Aufruf der Scoringliste
			zahl = sorte[1]
			if (sorte[0] == 4):						# Abfrage nach Wassermenge
				sorte[1] = round(zahl-(zahl/100*y))			# Scoringwert wird reduziert
			elif (sorte[0] == 1) or (sorte[0] == 5):
				sorte[1] = round(zahl-(zahl/150*y))			# Scoringwert wird reduziert
			elif (sorte[0] == 2):
				sorte[1] = round(zahl-(zahl/180*y))			# Scoringwert wird reduziert
			elif (sorte[0] == 6):
				sorte[1] = round(zahl-(zahl/200*y))			# Scoringwert wird reduziert
			else:
				sorte[1] = round(zahl-(zahl/220*y))			# Scoringwert wird reduziert
		return(scoringList)
	
	def daytime(liste, date):
		# =====================================================================
        	# MethodPurpose: Funktion zum Ermitteln und werten der typischen Beliebtheit von Produkten nach Tagezeiten.
		# Input: Kaffeeliste, Timestamp
		# Output: Scouringliste (liste)
        	# =====================================================================
		hour = int(date.strftime("%H"))						# bestimmen der Stunde zur Bestellung
		if (hour > 5) & (hour < 13):						# sortiert nach Tageszeit
			for element in liste:
				if (element[0]==1) or (element[0]==5):			# Auswahl Kaffee und Milchkaffee
					element[1] +=2					# Scoringwert steigt um 2
		elif (hour >= 13) & (hour < 18):
			for element in liste:						# Auswahl Espresse
				if (element[0]==3) or (element[0]==6):
					element[1] +=2					# Scoringwert steigt um 2
		else:
			for element in liste:
				if (element[0]==2) or (element[0]==4):			# Auswahl von Latte und heißem Wasser
					element[1] +=2					# Scoringwert steigt um 2
		return(liste)								# Bestimmung der Zeitzone um daraus Prios zu setzen
				
	def popularity(liste, bestellliste):
		# =====================================================================
        	# MethodPurpose: Funktion sortiert die Getränke nach Beliebtheit
		# Input: Kaffeeliste, Bestellliste
		# Output: Scouringliste (liste)
        	# =====================================================================
		zaehler = [0,0,0,0,0,0]
		drinkID = 1								# Zahlenwert wird festgelegt
		for j in zaehler:							# Dictionary wird erstellt Key=ID des Getränks, Value=Anzahl der Bestellungen
			zahl = drinkID-1
			bestellliste[drinkID] = zaehler[zahl]
			drinkID += 1
		bestellung = [(val,key)for key,val in dictonary.items()]		# Dictionary wird in Liste umgewandelt [(),(),...]	
		bestellung.sort()							# Dictionary wird nach Anzahl (Value) zunächst aufsteigend und anschließend absteigend sortiert
		bestellung.reverse()
		beliebtheit = []	
		for k in bestellung:							# IDs der Kaffees werden nach Beliebtheit in der Liste Beliebtheit eingeordnet
			beliebtheit.append(k[1])					# Rating wird in ScoringListe addiert
		zahl = 6
		for element in beliebtheit:						# muss noch kommentiert werden ##########################################
			listenwert = element-1
			aktuellerScore = liste[listenwert][1]
			neuerScore = aktuellerScore + zahl
			liste[listenwert][1] = neuerScore
			zahl = zahl - 1
		return(liste)
                        
	def powersaver(date):
		# =====================================================================
        	# MethodPurpose: Funktion um Kaffeemaschine in den Nachtmodus zu setzen
		# Input: Timestamp
		# Output: Tagezeit
        	# =====================================================================
		hour = int(date.strftime("%H"))						# bestimmen der Stunde zur Bestellung
		if(hour > 22) & (hour <5):						# schaltet zwischen 22 - 5 Uhr MASCHINE aus
			return False
		else:
			return True
			
	def decision(date):
		# =====================================================================
        	# MethodPurpose: Entscheidung, ob die Milch nachgefüllt werden soll
		# Input: Timestamp
		# Output: Wochentag
        	# =====================================================================
		weekday = date.weekday()						# bestimmt den Wochentag der Bestellung
		if (weekday < 3):							# nachgefüllt wird Mo., Di. & Mi.
			return True
		else:
			return False


