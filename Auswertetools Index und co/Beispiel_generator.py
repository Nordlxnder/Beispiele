#!/usr/bin/env python
# -*- coding: utf-8 -*-

y=[23.4,25.2,27.5, 28.0,22.9,21.2]
startwert=0
endwert=len(y)

def generator_1(daten,startwert,endwert):
    for x in daten[startwert:endwert]:
        yield x

gen1=generator_1(y,startwert,endwert)
for x in gen1:
    print(x)

#############################################
def generator_2(daten):
    for w in range(len(daten)):
        yield w

gen2=generator_2(y)
for x in gen2:
    print(x)

gen1=generator_1(y,startwert,endwert)
gen2=generator_2(y)
datensatz=list(zip(gen1,gen2))
print(datensatz)

################# send ########################

def generator_3():
    y = [23.4, 25.2, 27.5, 28.0, 22.9, 21.2]
    for x in y:
        yield x

gen3=generator_3()

print("send",gen3.send(None))
print("send2:",gen3.send(1))
for x in gen3:
    print("gen3:\t",x)


############### enumerate #########################





if __name__ == "__main__":
    pass