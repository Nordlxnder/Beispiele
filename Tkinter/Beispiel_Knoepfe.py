#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# damit es keine Fehlermeldungen wegen Sonderzeichen gibt

import tkinter
from tkinter import ttk
from tkinter import *
from tkinter import font

fenster=Tk()

# Anzeigen der Schriftarten
A=font.families()
print(A)

# moegliche Darstellungen 'clam', 'alt', 'default', 'classic'
themen=ttk.Style()
themen.theme_use('clam')



# Relief styles ö
# Beispiel flat, raised, sunken , groove, ridge, solid    3D Effect
Aussehen1 = ttk.Style()
Aussehen1.configure("MeinStil2.TButton", padding=20, relief="sunken",foreground="black", background="#adf")
Aussehen2 = ttk.Style()
Aussehen2.configure("MeinStil3.TButton", padding=20, relief="groove",foreground="blue", background="#3a1",font=('DejaVu Serif',30))

knopf1 = ttk.Button(text='OK',style="MeinStil3.TButton")
knopf2 = ttk.Button(text='Schliessen', command=fenster.quit, cursor='trek')
knopf3 = ttk.Button(text='OK 2',style='MeinStil2.TButton')
knopf4 = ttk.Button(text='Test 2',style="MeinStil3.TButton")
knopf5=Button(text='TK',relief=RAISED,\
                        cursor="plus")

# Der Knopf wird angezeigt
knopf1.pack()

# Der Knopf wird mit einem Rand angezeigt
knopf2.pack(pady=8,padx=20)

knopf3.pack(pady=8,padx=40)

# Anzeige mit einer bestimmten Schriftart Schriftart
knopf4.pack(pady=8,padx=20)
knopf5.pack(pady=8,padx=8)
mainloop()