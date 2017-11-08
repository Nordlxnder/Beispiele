#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# damit es keine Fehlermeldungen wegen Sonderzeichen gibt
#import tkinker
import tkinter
from tkinter import ttk
from tkinter import *

fenster=Tk()


# Hintergrundfarbe einstellen

stil1 = ttk.Style()
stil1.configure('R1.TButton', background='maroon')

stil2 = ttk.Style()
stil2.configure('R2.TButton', background='green')

# Relief styles
# Beispiel flat, raised, sunken , groove, ridge, solid    3D Effect
rahmen1=ttk.Frame(fenster, borderwidth=5, relief="sunken", width=200, height=100, style='R1.TButton')
rahmen2=ttk.Frame(fenster, borderwidth=5, relief="raised", width=200, height=100)
rahmen3=ttk.Frame(fenster, borderwidth=5, relief="groove", width=200, height=100)
rahmen4=ttk.Frame(fenster, borderwidth=15, relief="ridge", width=200, height=100,style='R2.TButton')
rahmen5=ttk.Frame(fenster, borderwidth=5, relief="solid", width=200, height=100)


# Zeichnen
rahmen1.pack()
rahmen2.pack()
rahmen3.pack()
rahmen4.pack()
rahmen5.pack()

mainloop()