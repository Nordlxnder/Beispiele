#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Beschreibung:
        Die ist ein Beispiel für die Live Anzeige eines Temperaturverlaufs
        mit LineCollection und Matplotlib.animation
'''

import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import matplotlib.dates as mdates
import matplotlib.animation as animation
from datetime import datetime

import numpy as np
from numpy import loadtxt as dateiladen


def daten_einlesen(zeitbereich="tag"):
    '''
    Einlesen der ASCII Datei Wetter.log

    Die Daten wurden in einem Raster von 5 min (=288 Punkte pro Tag) aufgezeichnet

    Zeit Aussentempratur1 Luftdruck Luftfeucht Höhe CPU-Temperatur
    s °C hPa % m °C
    1509206209 10,8 1019 57 83,2 25,6
    1509206212 10,8 1019 57 83,0 26,1
    1509210120 10,9 1018 57 82,2 26,1

    :param zeitbereich: string vVorgabewert um nur einen Zeitbereich anzuzeigen
    :return:
    '''
    zeit, aussentemp = dateiladen("wetter.log", delimiter=" ", skiprows=2,
                                  converters={1: lambda wert: wert.replace(",", ".")},
                                  encoding="utf-8", usecols=(0, 1), unpack=True)

    # Zeitbereich der letzten 24 Stunden
    if zeitbereich == "tag":
        zeit = zeit[-288:]
        aussentemp = aussentemp[-288:]

    return zeit, aussentemp


class OnlineDiagramm():
    def __init__(self,
                 x_spur = np.array([1, 2]),
                 y_spur = np.array([4, 8]),
                 typ_x_spur = "",
                 farbe_og = 30,
                 farbe_ug = 24,
                 bar = False,
                 intp = 1,
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

            typ_x_spur="unixzeit",
                    Wenn die Werte der X-Spur aus der Unixzeitwerten besteht kann
                    kann x_datum auf "unixzeit" gesetzt werden und die X-Achse
                    wird dann angepasst auf einen Tages verlauf
            farbe_og=30,
                    Maximalwert für die Farbe der Oberengrenze
            farbe_ug=24,
                    Maximalwert für die Farbe der Unterengrenze
            intp  = 1
                    intp ist die Anzahl der Punkt die hinzugefügt bzw. Interpoliert
                    werden soll. Der Wert muss ein Integer sein.
                    Ist der Wert 1 passiert nichts
            bar=True
                    seitliche Anzeige des Farbverlaufs über den Wertebereich
        '''

        self.x_spur = x_spur
        self.y_spur = y_spur
        self.farbe_og = farbe_og
        self.farbe_ug = farbe_ug
        self.bar = bar
        self.typ_x_spur = typ_x_spur
        self.fontsize=10
        self.intp = intp

        ### Funktionen ###

        # List oder Tuple Daten in numpy.array konvertieren
        self.daten_pruefen_und_konvertieren()

        # Daten interpolieren für besseren Farbverlauf
        if intp > 1:
            self.daten_interpolieren(int(intp))

        # Diagramm erstellung
        self.abbildung = plt.figure()
        self.diagramm = self.abbildung.add_subplot(1, 1, 1)

        # Diagrammgestalltung
        self.linien_sammlung()
        self.diagramm_gestaltung()

        # Animation
        ani = animation.FuncAnimation(self.abbildung,
                            self.animate,
                            interval=refresh_interval,
                            init_func=self.init,
                            blit=False, save_count=5)

        plt.show()

    def daten_pruefen_und_konvertieren(self):
        '''
        Datentyp prüfen

        wenn der Datentyp List oder Tuple ist, wird daraus ein numpy array

        :return:
        '''

        if isinstance(self.x_spur, list) or isinstance(self.x_spur, tuple):
            self.x_spur = np.array(self.x_spur)

        if isinstance(self.y_spur, list) or isinstance(self.y_spur, tuple):
            self.y_spur = np.array(self.y_spur)

    def x_spur_von_unixzeit_zu_datetime(self):

        '''
        Konvertierung der Daten der X-Spur wenn sie Uniszietstemple enthalten
        Dies ist notwendig damit Linecollection damit arbeiten kann
        :return:
        '''

        # Schritt 1 konvertieren von Unixzeit zu datetime
        x = []
        [x.append(datetime.fromtimestamp(int(e))) for e in self.x_spur]

        # Schritt 2 da linecollection nur mit float arbeiten kann,
        # wird datetime zu num konvertiert
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

        # # Hintergrundfarbe
        diagramm.set_facecolor('grey')

        # Raster
        diagramm.grid(True)


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

    def init(self):
        diagramm = self.diagramm

        diagramm.grid(True)

        # Objekt Liniensammlung neu erstellen und anzeigen im Diagramm
        self.linien_sammlung()

        self.x_und_y_achse_neu_skalieren()

        if self.bar == True:
            # hinzufügen der Anzeige für die Farbskala
            self.abbildung.colorbar(self.line, ax=diagramm)

        return self.line,

    def animate(self,count):
        diagramm = self.diagramm

        # Daten im Diagramm löschen bevor neu gezeichnet wird
        diagramm.clear()
        # diagramm.grid(True)

        # Daten aus der Datei neu einlesen
        self.daten_aktualisieren()

        # Daten interpolieren für besseren Farbverlauf
        if self.intp > 1:
            self.daten_interpolieren(int(self.intp))

        # Unixzeit- Konvertierung
        if self.typ_x_spur == "unixzeit":
            self.x_spur_von_unixzeit_zu_datetime()
            self.diagramm_gestaltung_mit_datum()

        # Objekt Liniensammlung neu erstellen und anzeigen im Diagramm
        self.linien_sammlung()
        self.diagramm_gestaltung()
        self.x_und_y_achse_neu_skalieren()

        return self.line,

    def daten_aktualisieren(self):
        self.x_spur, self.y_spur = daten_einlesen()

    def x_und_y_achse_neu_skalieren(self):
        '''
        Neuskalierung der X-Achse bzw. Y-Achse
        '''
        diagramm = self.diagramm
        # X und Y Zoom
        diagramm.set_xlim(self.x_spur.min(), self.x_spur.max())
        diagramm.set_ylim(self.y_spur.min(), self.y_spur.max())


def hauptprogramm():

    diagramm=OnlineDiagramm(typ_x_spur="unixzeit", bar = True,
                            intp=200, refresh_interval=10000)


if __name__ == "__main__":
    hauptprogramm()
