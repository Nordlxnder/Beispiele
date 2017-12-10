#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

pfad="/home/golfo/PycharmProjects/dateiname_in_utf-8_konvertieren/dateien/"

def dateien_einlesen():
    dateien = os.listdir(pfad)
    print(dateien)
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