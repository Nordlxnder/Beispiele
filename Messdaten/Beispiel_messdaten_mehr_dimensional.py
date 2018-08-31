#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import array,where
from numpy import transpose as drehen


messdaten_2dim=((1.1,0),
                (2.0,1),
                (3.2,2),
                (4.2,3))
messdaten_3dim=((1.1,0,29),
                (2.0,1,30),
                (3.2,2,30),
                (4.2,3,31))
# messdaten=(((1.1,0),((2.0,1),30),((3.2,2),30),((4.2,3),31))
# messdaten=(1.1,2.0,3.2,4.2)
zeitdaten=(1,2,3,4)
datum_tag=[29,30,30,31]

def zwei_dimensionen():
    print("\n  ### 2 Dimensionen ### \n")

    dim2=array(messdaten_2dim)
    print(dim2)

    print("\n  ##################### \n")

    print("Datentyp:\t",dim2.dtype)
    print(dim2.itemsize)
    print(dim2.shape)
    print(dim2.size)
    print(dim2.nbytes)  # number of bytes

def drei_dimensionen():
    print("\n  ### 3 Dimensionen ### \n")
    dim3=array(messdaten_3dim)

    print(dim3)
    print("\n  ##################### \n")

def mask_tag():
    dim3 = array(messdaten_3dim)
    stichtag=dim3[:,-1]
    tag=29
    mask=where(stichtag==tag)
    daten=dim3[mask,:]
    print(mask)
    print("\n  ##################### \n")
    print(daten)
    print("\n  ##################### \n")
    print(daten[:,:,0:2])

def dim3_drehen():
    print("\n  ### 3 Dimensionen ### \n")

    dim3 = array(messdaten_3dim)

    print("Ausgangsmatrix\n\n",dim3)

    print("\n\n##### gedrehte Matrix ###### \n")
    print(drehen(messdaten_3dim))

    print("\n##################### \n")

def hauptprogramm():

    # zwei_dimensionen()
    # drei_dimensionen()
    # mask_tag()
    dim3_drehen()
    print("\ntue nichts!!\n")
    pass


if __name__=="__main__":
    hauptprogramm()