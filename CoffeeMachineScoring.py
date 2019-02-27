import time

prio = "immer"

def perishablemilk():
	a = 6
	#a ist x Wert.
	#Wird von Milchstand geliefert und gibt den Prozentsatz des Füllstands wieder (0-10)
	y = 0.18*1.5**a
	#exponential Funktion f(x)=0.18 * 1.5**x

	return(int(y))

def daytime():
	
	hour = int(time.strftime("%H"))
	print (hour)
	prio = "test"
	#warum rechnet er nicht die if Funktionen?
	if (hour > 5) & (hour < 13):
		prio = "morgens"
	elif (hour > 13) & (hour < 18):
		prio = "mittags"
	else:
		prio = "abends"
	return (prio)
