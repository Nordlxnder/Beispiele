#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os

'''
Dieses Programm ändert die Zeichen einer Datei die mit Raute Fragezeichen 
dargestellt werden

Beispiel:

01_Testdatei_�.txt  oder '01_Testdatei_'$'\372''.txt'

'''

pfad=str(os.path.abspath(os.curdir) + "/dateien/")
def dateien_einlesen():
    dateien = os.listdir(pfad)
    # print(dateien)
    return dateien

def umbenennen(dateien):
    # Konvertirierung der Umlaute bzw Sonderzeichen
    dateien_neu=[ str(dateien[e]).encode('utf-8', 'surrogateescape').decode('ISO-8859-1')
                  for e in range(0,len(dateien))]
    # Umbenennung der Dateien
    [os.rename(pfad+dateien[e],pfad+dateien_neu[e]) for e in range(0,len(dateien))]
    # print(dateien_neu)
    pass

def hauptprogramm():
    dateien=dateien_einlesen()
    umbenennen(dateien)
    pass

if __name__== "__main__":
    hauptprogramm()