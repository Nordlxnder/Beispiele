#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# coding: utf8
# damit es keine Fehlermeldungen durch Sonderzeichen gibt
import tkinter
from tkinter import ttk
from tkinter import *

fenster=tkinter.Tk()
fenster.title("CANBUS-Ausgabe")

# Vorgabe der Groesse des Fensters und der Position
#
'''
def Fenster():
    Breite = 800 # Breite des Fensters
    Hoehe  = 480
    x= 900
    y= 300
    fenster.geometry('%dx%d+%d+%d' % (Breite, Hoehe, x, y))

Fenster()
'''
class Anzeigen:
    def __init__(self):
        self.Breite = 800 # Breite des Fensters
        self.Hoehe  = 480
        self.x= 900
        self.y= 300
        fenster.geometry('%dx%d+%d+%d' % (self.Breite, self.Hoehe, self.x, self.y))



Hauptfenster=Anzeigen()


Rahmen1 = LabelFrame(fenster, text="Dies ist ein Rahmen")

Rahmen_innen_1 = LabelFrame(Rahmen1, text="Wert 1")
Rahmen_innen_2 = LabelFrame(Rahmen1, text="Wert 2")
Rahmen_innen_3 = LabelFrame(Rahmen1, text="Wert 3")
Rahmen_innen_4 = LabelFrame(Rahmen1, text="Wert 4")

Rahmen1.grid(column=0, row=0, padx=20, pady=20)
Rahmen_innen_1.grid(column=0, row=0, padx=10, pady=10)
Rahmen_innen_2.grid(column=0, row=1, padx=10, pady=10)
Rahmen_innen_3.grid(column=1, row=0, padx=10, pady=10)
Rahmen_innen_4.grid(column=1, row=1, padx=10, pady=10)


Anzeige1=Label(Rahmen_innen_1,text="Textmeldung 1",anchor='e')
Anzeige2=Label(Rahmen_innen_2,text="Textmeldung 2")
Anzeige3=Label(Rahmen_innen_3,text="Textmeldung 3")
Anzeige4=Label(Rahmen_innen_4,text="Textmeldung 4")

Anzeige1.grid(column=0, row=0, padx=0, pady=0)
Anzeige2.grid(column=0, row=0, padx=50, pady=50)
Anzeige3.grid(column=0, row=0, padx=50, pady=50)
Anzeige4.grid(column=0, row=0, padx=50, pady=50)


mainloop()