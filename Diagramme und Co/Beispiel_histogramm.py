#!/usr/bin/env python
# -*- coding: utf-8 -*-


import numpy as np
from io import BytesIO
import matplotlib.pyplot as plt
import os

### Daten einlesen
pfad=os.chdir("./log/")
dateiname="adidas.csv"
beginn_daten=2


with open(dateiname, "r") as datei:
    # Datei wird eingelesen und Kommas durch einen Punkt ersetzt
    # encode macht aus dem String wieder ein ByteString (binary stream)
    # dies wird von genfromtxt zum einlesen benötigt
    # BytesIO erzeugt ein benötigtes Byte Objekt
    daten=datei.read().replace(",",".").encode("utf-8")
datum, akt_wert, akt_min, akt_max =np.genfromtxt(BytesIO(daten), delimiter=";", unpack=True, skip_header=beginn_daten)

#### ## Graph Diagrammanzeige #### ##

x=akt_wert

x_min= min(x)
x_max= max(x)
# print(x)
# the histogram of the data

bins=[180,181,182,183,184,185,190,195,200]
# n, bins, patches = plt.hist(x, bins=bins , normed=1, facecolor='g', rwidth=0.8 ,alpha=0.75)
n, bins, patches = plt.hist(x, bins=25 , normed=1, facecolor='g', alpha=0.75)

# Histogramm

# print(n)
# print(bins)
# print(patches)
plt.xlabel('Schwerpunkt')
plt.ylabel('Häufigkeit')
plt.title('Überschrift')
plt.text(180, .125, r'Letzterwert: '+str(x[-1]))
plt.axis([x_min, x_max, 0, 0.2])
plt.grid(True)
plt.show()

def hauptprogramm():

    print ("Hauptprogramm Graph wurde ausgeführt!")
    pass


if __name__ == "__main__":
    hauptprogramm()