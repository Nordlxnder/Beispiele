#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Beschreibung:
        Die ist ein Beispiel um einen Farbverlauf für ein Messsignal
        mit LineCollection anzuzeigen
'''

import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import matplotlib.dates as mdates
from datetime import datetime

import numpy as np


class OnlineDiagramm():
    def __init__(self,
                 x_spur=np.array([1, 2]),
                 y_spur=np.array([20, 40]),
                 x_datum="",
                 farbe_og=30,
                 farbe_ug=24,
                 bar=False,
                 intp=1,
                 refresh_interval=1000
                 ):
        '''
        Parameter:
            x_spur=np.array([1, 2]),
            y_spur=np.array([4, 8]),
                    Kann vom Typ List, Tuple oder NumpyArray sein
                    x_spur = np.array([1, 2, 3, 4, 5])
                    y_spur = np.array([10,40,30,50,-10])
                    x_spur = (1, 2, 3, 4, 5)
                    y_spur = [10,40,30,50,-10]

            x_datum="unixzeit",
                    Wenn die Werte der X-Spur aus der Unixzeitwerten besteht kann
                    kann x_datum auf "unixzeit" gesetzt werden und die X-Achse
                    wird dann angepasst auf einen Tages verlauf
            farbe_og=30,
                    Maximalwert für die Farbe der Oberengrenze
            farbe_ug=24,
                    Maximalwert für die Farbe der Unterengrenze
            intp  = 1
                    Wert sollte immer ein Integerwert sein. Wenn der Wert gößer 1
                    um diesen Faktor Interpoliert. Ist der Wert 1 passiert nichts
            bar=True
                    seitliche Anzeige des Farbverlaufs über den Wertebereich
        '''

        # Datentyp prüfen

        # wenn der Datentyp List oder Tuple ist, wird daraus ein numpy array

        if isinstance(x_spur,list) or isinstance(x_spur,tuple):
            self.x_spur = np.array(x_spur)
        else:
            self.x_spur = x_spur
        if isinstance(y_spur,list) or isinstance(x_spur,tuple):
            self.y_spur = np.array(y_spur)
        else:
            self.y_spur = y_spur

        if intp > 1:
            self.daten_interpolieren(int(intp))  # Für besseren Farbverlauf

        self.farbe_og = farbe_og
        self.farbe_ug = farbe_ug
        self.bar = bar

        self.fontsize=10

        self.abbildung = plt.figure()

        self.diagramm = self.abbildung.add_subplot(1, 1, 1)

        if x_datum == "unixzeit":
            self.x_spur_von_unixzeit_zu_datetime()
            self.diagramm_gestaltung_mit_datum()    # Anpassung für die X-Achse

        self.linien_sammlung()
        self.diagramm_gestaltung()

        plt.show()

    def x_spur_von_unixzeit_zu_datetime(self):

        # Datenkonvertieren damit Linecollection damit arbeiten kann
        # Schritt 1 konvertieren von Unixzeit zu datetime
        x = []
        [x.append(datetime.fromtimestamp(int(e))) for e in self.x_spur]

        # Da linecollection nur mit float arbeiten kann, wird datetime zu num konvertiert
        self.x_spur = mdates.date2num(x)

    def daten_interpolieren(self, intp):
        '''
        Daten interpolieren damit der Farbverlauf feiner wird
        :return:
        '''

        x_range = np.linspace(self.x_spur.min(), self.x_spur.max(),
                              len(self.x_spur)*intp)

        y_range = np.interp(x_range, self.x_spur, self.y_spur)

        self.x_spur = x_range
        self.y_spur = y_range

    def linien_sammlung(self):
        diagramm = self.diagramm

        x_y_daten = np.array([self.x_spur, self.y_spur]).T.reshape(-1, 1, 2)
        segmente = np.concatenate([x_y_daten[:-1], x_y_daten[1:]], axis=1)

        # Create a continuous norm to map from data points to colors
        norm = plt.Normalize(self.farbe_ug, self.farbe_og)

        # Auswahl des Farbverlaufs
        cmap = 'viridis'
        cmap = 'RdYlGn'  # Rot Gelb Grün
        cmap = 'RdYlGn_r'  # Rot Gelb Grün
        cmap = 'hsv'     # Regenbogen

        line_collection = LineCollection(segmente, cmap=cmap, norm=norm)

        # Farbzuordnung der Y-Werte,
        # hier wird entschieden auf welchen Wert der Farbverlauf angewendet werden soll
        line_collection.set_array(self.y_spur)

        # hinzufügen der Liniensammlung
        self.line = diagramm.add_collection(line_collection)

    def diagramm_gestaltung_mit_datum(self):
        '''
                 Anpassung für die X-Achse
                 Datumsformatierung der X Achse
        '''
        diagramm = self.diagramm

        # X-Achse
        diagramm.xaxis.set_major_formatter(mdates.DateFormatter("%d %b %H:%M"))
        diagramm.set_xlabel("Uhrzeit", fontsize=self.fontsize + 6)

        stunde = mdates.HourLocator(interval=6)
        stunde1 = mdates.HourLocator(interval=1)

        diagramm.xaxis.set_major_locator(stunde)
        diagramm.xaxis.set_minor_locator(stunde1)


    def diagramm_gestaltung(self):
        diagramm = self.diagramm

        # Diagramm

        # Hintergrundfarbe
        diagramm.set_facecolor('grey')

        # Überschrift
        diagramm.set_title("Überschrift")

        diagramm.set_ylabel("Signalname und Einheit")

        diagramm.set_xlabel("BasisSignalname und Einheit\n"
                            "z.B. Zeit in [s]")

        # Raster
        diagramm.grid(True)

        if self.bar == True:
            # hinzufügen der Anzeige für die Farbskala
            self.abbildung.colorbar(self.line, ax=diagramm)

        # X und Y Zoom
        diagramm.set_xlim(self.x_spur.min(), self.x_spur.max())
        diagramm.set_ylim(self.y_spur.min(), self.y_spur.max())


def hauptprogramm():
    # x = np.array([1,2,3,4,5])
    # y = np.array([10,40,30,50,-10])
    #
    # x, y = daten_einlesen()
    #
    # # Daten interpolieren damit der Farbverlauf feiner ist
    # x_range = np.linspace(x.min(), x.max(), len(x)*200)
    # y_range = np.interp(x_range, x, y)
    #
    # graph(x_range,y_range,"unixzeit",bar=True)
    # # graph(x_range,y_range,"",farbe_og=40,farbe_ug=0)
    diagramm=OnlineDiagramm(bar=True,intp=200)


if __name__ == "__main__":
    hauptprogramm()
