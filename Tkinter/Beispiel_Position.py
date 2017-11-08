#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# damit es keine Fehlermeldungen durch Sonderzeichen gibt

import tkinter
from tkinter import ttk
from tkinter import messagebox
from tkinter import *

fenster=tkinter.Tk()
fenster.title("Hallo")
#                Breite x Höhe  +1000+ 400 Position
fenster.geometry("300x200+100+400")

# Fenster2  in die Mitte setzen

fenster2=tkinter.Tk()
fenster.title("Fenster 2")
w = 800 # Breite des Fensters
h = 650 # Höhe des Fensters

# Abfrage der Höhe und Breite des Monitors
ws = fenster2.winfo_screenwidth() # width of the screen
hs = fenster2.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# setzt die dimension des Fensters
# und den Platz
fenster2.geometry('%dx%d+%d+%d' % (w, h, x, y))





mainloop()