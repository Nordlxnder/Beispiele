#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# damit es keine Fehlermeldungen wegen Sonderzeichen gibt

import tkinter
from tkinter import ttk
from tkinter import *
import threading
import time

def threadfunc():
    i=1
    while True:
        time.sleep(1)
        print("%s Sekunden mehr" % (i))
        i+=1
th = threading.Thread(target=threadfunc)
th.daemon = True
th.start()



fenster=tkinter.Tk()
fenster.title("CANBUS-Ausgabe")

# Vorgabe der Groesse des Fensters und der Position
#
def Fenster():
    Breite = 800 # Breite des Fensters
    Hoehe  = 480
    x= 900
    y= 300
    fenster.geometry('%dx%d+%d+%d' % (Breite, Hoehe, x, y))

Fenster()

mainloop()