#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# coding: utf8
# damit es keine Fehlermeldungen durch Sonderzeichen gibt

# Liesst die Datei ein

#Datei = open("cantest2.log")
#A=Datei.read()
#print (A)
#Datei.close()

# Beispiel 2 einlesen und Zeile 1 und 2 ausgeben
#    Datei_in = open("cantest2.log",'r')
#    print (Datei_in)
#    print(Datei_in.readline())
#    print(Datei_in.readline())
#    Datei_in.close()


#Beispiel 3 auslesen und ersetzen
Dateiname = 'cantest2.log'
Datei_in = open(Dateiname, 'r')
Datei_out= open("cantest2_aus.log",'w')
i=0
while Datei_in.readline(): ## how to check that end is reached?
    s = Datei_in.readline()
    if Datei_in.readline()=="":
        break
    #print (s)
    B=s.split(" ")
    print(B)
    Zeitstempel='{:f}'.format(float(i*0.005)+0.000001)
    N='(' + Zeitstempel + ') ' + str(B[1]) + " "+ B[3]
    Datei_out.write(N)
    i+=1
    print(i)
    print (Zeitstempel)

Datei_in.close()
Datei_out.close()