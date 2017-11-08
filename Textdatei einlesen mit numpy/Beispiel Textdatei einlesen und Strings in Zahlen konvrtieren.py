#!/usr/bin/env python
# -*- coding: utf-8 -*-


import numpy as np
import datetime
from io import BytesIO

'''
Zeit Aussentempratur1
s °C 
1509206209 10,8
1509206212 10,8
1509210120 10,9
'''
# b'10,8' der binäre Wert wird erst in ein String gewandelt dann wird die Stringoperation ersetzen
# benutzt um das Komma gegen den Punkt auszutauschen und dann wird der String in eine Zahl gewandel mit float
# convertfunc = lambda x: print(x)

convertfunc = lambda x: float(x.decode("utf-8").replace(",","."))

konvert_zeit= lambda t: datetime.datetime.fromtimestamp(int(t))

dateiname="test.txt"
beginn_daten=2
namen=("X","Y")

with open(dateiname, "r") as datei:
    # Datei wird eingelesen und Kommas durch einen Punkt ersetzt
    # encode macht aus dem String wieder ein ByteString (binary stream)
    # dies wird von genfromtxt zum einlesen benötigt
    # BytesIO erzeugt ein benötigtes Byte Objekt
    daten=datei.read().replace(",",".").encode("utf-8")

datum, temp =np.genfromtxt(BytesIO(daten), delimiter=" ", unpack=True, skip_header=beginn_daten)

# Beispiel für eine Funktion zur Umrechnung der Unix Zeit in eine Standard Zeit
def kovertieren_in_zeit(zeit):
    x_zeit=[]
    for t in zeit:
        x_zeit.append(datetime.datetime.fromtimestamp(t))
    return x_zeit

# Beispiel für die gleiche Funktion als Lambda Funktion
f= lambda zeit : datetime.datetime.fromtimestamp(zeit)
    # map sorgt dafür das die Funktion auf jedes einzelne Element in
    # in der Liste angewendet wird und list erzeugt daraus wieder eine Liste
x_spur=list(map(f, datum))

print("Datum:\t",kovertieren_in_zeit(datum))
print("Ausssentemperatur:\t", temp)
print("Datum x_spur:\t",x_spur)

if __name__ == "__main__":
    pass