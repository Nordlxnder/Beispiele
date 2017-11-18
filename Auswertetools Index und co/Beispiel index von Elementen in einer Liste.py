#!/usr/bin/env python
# -*- coding: utf-8 -*-

a=[2,3,5,7,3,4,2,3,2,3,3,33333,"test",2]

print("\nverwendete Liste:\t",a,"\n")

# gibt die Position des ersten Auftretens des Elements in der Liste zurück
b=a.index(3)
print("Position des ersten Auftreten in der Liste:\t",b)

# gibt den Index aller Positionen des Elements in der Liste an
c=[index for index, v in enumerate(a) if v == 2]
print("Positionen des Elements in der Liste: \t",c)

# gibt dden Index aller Positionen des Elements in der Liste an
d=[index for index, v in enumerate(a) if v == "test"]
e=[index for index, v in enumerate(a) if v == "xyz"]
print("Position des Element in der Liste:\t",d, "\tRückgabewert des Elements das nicht in der Liste ist:\t", e)

# Vergleich der Elemente in der Liste

#f= [i for i,wert in a: if wert >= 3]
for wert in a:
    if wert >= 3:
        print(wert)
#print(f)




if __name__ == "__main__":
    pass