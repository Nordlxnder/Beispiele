#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt


x=[0,1,2,3,4,5,6,7,8,9,10]
y=[3,7,3,7,8,2,5,1,6,9,4]

# als dictinary
x2 ={"X-achse": x}
y2 ={"Y-Achse": y}


def diagramm_zeichnen(x,y):
    # Ermöglicht die Gestaltungsoption zu setzen
    fig= plt.figure()
    xachse1=plt.subplot2grid((1,1),(0,0))

    # linestyle=":"
    # linestyle="._"
    # linestyle="--"
    linestyles = ['-', '--', '-.', ':']
    xachse1.plot(x, y, linestyle=linestyles[2],marker="o", color="b",label="Labeltext")
    # print(help(xachse1.plot))
    plt.xlim(0,10)
    plt.ylim(0,10)

    # Raster einschalten und konfigurieren
    xachse1.grid(True)#,color="g",linestyle="-",linewidth=3)

    # Abstand des Diagramm vom Fensterrand und
    # Abstand untereinander bei mehreren Diagrammen
    plt.subplots_adjust(left=0.1,bottom=0.18,right=0.90,top=0.90, wspace=2, hspace=0 )

    # die x-Achsenbeschriftung wird um 45 Grad gedreht
    for label in xachse1.xaxis.get_ticklabels():
        label.set_rotation(45)

    # Beschriftung
    plt.title("Überschrift")
    plt.xlabel("x-Achse")
    plt.ylabel("y-Achse")

    plt.show()
    pass


def diagramm2_dic(x2,y2):
    ''' Daten liegen als Dictionary vor'''
    fig = plt.figure()
    xachse1 = plt.subplot2grid((1, 1), (0, 0))
    # print(help(xachse1.plot))
    x=list(x2.values())[0]
    y=list(y2.values())[0]
    xachse1.plot(x, y, ":", marker="o", color="b", label="Legendentext")
    plt.xlabel(list(x2.keys())[0])
    plt.ylabel(list(y2.keys())[0])
    plt.legend() # Zeigt die Bezeichnung des Labels an
    plt.show()
    pass


def hauptprogramm():
    diagramm_zeichnen(x,y)
    diagramm2_dic(x2,y2)
    print("Hauptprogramm wurde ausgeführt!")
    pass


if __name__=="__main__":
    hauptprogramm()