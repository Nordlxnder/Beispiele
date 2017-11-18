#!/usr/bin/env python
# -*- coding: utf-8 -*-

a=[2,3,5,7,3,4,2,3,2,3,3,33333,"test",2]

print(a)

# gibt die Position des ersten auftretens des Elements in der Liste zurück
b=a.index(3)
print(b)

# gibt dden Index aller Positionen des Elements in der Liste an
c=[index for index, v in enumerate(a) if v == 2]
print(c)

# gibt dden Index aller Positionen des Elements in der Liste an
d=[index for index, v in enumerate(a) if v == "test"]
e=[index for index, v in enumerate(a) if v == "xyz"]
print("Position des Element in der Liste:\t",d, "\tElement des nicht in der Liste ist:\t", e)


if __name__ == "__main__":
    pass