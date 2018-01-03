#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def verzeichnis_pruefen(pfad):

    verzeichnisse=pfad.split("/")
    for i in range(1, len(verzeichnisse)):
        if len(verzeichnisse[i]) != 0:
            # prüfen ob das Verzeichnis vorhanden ist an sonsten erstellen
            try:
                os.makedirs(verzeichnisse[i], mode=0o744, exist_ok=False)
            except OSError as fehler:
                # print(fehler)
                print("Verzeichnis " + verzeichnisse[i] + " existiert bereits!\n")
        # wechseln in das Verzeichnis
        os.chdir("./" + verzeichnisse[i])

def hauptprogramm():

    pfad="./log/ordner1/ordner2/ordner3"
    verzeichnis_pruefen(pfad)

    print("Das Hauptprogramm wurde ausgeführt!")


if __name__== "__main__":
    hauptprogramm()