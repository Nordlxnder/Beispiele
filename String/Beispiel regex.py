#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
'''
    Das Skript zeigt einige Beispiele reguläre expression

'''

data='<a href="/aktien/Daimler-Aktie">Daimler</a><br /><a class="color-grey" href="/aktien/Daimler-Aktie">DE0007100000</a>'

# zeigt die Daten
daten=re.findall(r'(.*)',data)
print("Daten:\t",daten)

# findet alles was kein Sonderzeichen ist
daten3=re.findall(r'([a-zA-Z0-9]*)',data)
print("Daten3:\t",daten3)

# findet alle Wörter , die mit einem großen D beginnen
daten4=re.findall(r'([D][a-zA-Z0-9_]*)',data)
print("Daten4:\t",daten4)


data2='<a href="/aktien/Deutsche_Boerse-Aktie">Deutsche B\xf6rse</a><br /><a class="color-grey" href="/aktien/Deutsche_Boerse-Aktie">DE0005810055</a>'
data2='<a href="/aktien/Munich_Re-Aktie">M\\xfcnchener R\\xfcckversicherungs-Gesellschaft</a><br /><a class="color-grey" href="/aktien/Munich_Re-Aktie">DE0008430026</a>'
print("Data2:\t",data2)

daten5=re.findall(r'([a-zA-Z0-9_]*)',data2)
print("Daten5:\t",daten5)

daten7=re.findall(r'([<].*)',data2)
print("Data2:\t\t",data2)
print("Daten7:\t\t",daten7)

# \xf6  = ö , \xe4 = ä , \xfc = ü
# Alle Werte bestehend aus a-z , A-Z , 0-9 , _ , Leerzeichen
daten8= re.findall(r'>([a-zA-Z0-9\xf6\xfc_ \\]*)',str(daten7))
#print("Daten8:\t", daten8[0])

# \\ wird ersetzt durch \
data3=re.sub(r'([.*]*)\\\\', r'\\', str(daten7))
data3=re.sub(r'([.*]*)\\xfc', r'ü', str(data3))
print("Replace:\t", data3)