#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# coding: utf8
# damit es keine Fehlermeldungen durch Sonderzeichen gibt

import socket
import struct
import threading ,sys
import binascii

'''
!!!!! HINWEIS fuer CANSEND!!!!
CAN Send Beispiel fuer Standard und Extended


cansend can1 -i 0x1F   0x11 0x22 0x33 0x44 0x55 0x55 0x77 0x88
cansend can1 -e -i 0x1F334455   0x11 0x22 0x33 0x44 0x55 0x55 0x77 0x88

cansend can1 1F#1122334455667788
cansend can1 1F334455#1122334455667788

'''


def start_canbus():

    can_interface = socket.socket(socket.AF_CAN, socket.SOCK_RAW, socket.CAN_RAW)
        # Name der Schnittstelle
    interface = "vcan0"
    try:
            # Herstellen der Verbindung zur Schnittstelle
            # "bind" benoetigt nur ein Argument deshalb wird
            # die Schnittstelle in doppelte Klammern gesetzt
        can_interface.bind((interface,))
        print("Verbindung mit vcan0 wurde hergestellt!")
        return (can_interface)

    except OSError:
        Warnmeldung="\n\
    can0 konnte mit der Schnittstelle \n\
    nicht verbunden werden! \n\
    Bitte pruefen Sie ob die Treiber\n\
    geladen sind!"
        print(Warnmeldung)

def canbus_Botschaft_lesen(can_interface):
        # .recv empfange Daten im Puffer in der Groesse von 16 Bytes
        # Hinweis 16 ist nicht ausreichend falls die Botschaft
        # im Format "extended" gesendet wird
    can_pkt = can_interface.recv(16)
    return(can_pkt)

def can_Botschaft_aufteilen(can_pkt):
        # > <     Byte-Reihenfolge
        #
        #    Format 	C Type 	        Python type 	Standard size
        #    I 	        unsigned int 	integer 	4
        #    B 	        unsigned char 	integer 	1
        #    x 	        pad byte 	no value
        #    s 	        char[] 	        bytes
        #
        #               4Bytes   1  3Bytes 2Bytes 2Bytes 2Bytes 2Bytes
        #               ________ __ ______ ____   ____   ____   ____
        # Botschaft: b' 64000000 08 000000 0001   0002   0003   0004'
        #fmt = "<IB3x8s"
        # print("Botschaft:", binascii.hexlify(can_pkt))
        # Botschaft: b'64000000080000000001000200030004'
        # 4 Werte a 16 bit
    FMT = "<IB3x2s2s2s2s"
    can_id, length, wert1, wert2, wert3, wert4 = struct.unpack(FMT, can_pkt)
    # Anzahl der Werte in der Botschaft
    Werteanzahl=int(float(length/2))
    return (can_id, Werteanzahl, wert1, wert2, wert3, wert4)

def can_Filter():
    # Der Filter pass wenn diese Bedingung erfüllt ist
    # <received_can_id> & mask == can_id & mask
    # id = 0x64
    #    000001100100    0x64
    #   &011111111111  &0x7FF
    #   _____________  ______
    #   =000001100100  = 0x64
    # mask = 0x700   entspricht 0b011100000000   alle Botschaften im hex Bereich von 00 bis FF
    # mask = 0x7FF   entspricht 0b011111111111   es wird nur eine bestimmte Botschaft
    # die ID besteht aus 11 bit damit 3 Hex Werte oder 000-7FF
    #        __7_ __F_ __F_
    # mask = 0111 1111 1111
    id = 0b000001100100
    mask = 0b011111111111
    can_interface.setsockopt(socket.SOL_CAN_RAW, socket.CAN_RAW_FILTER,struct.pack("II", id, mask))


if __name__=='__main__':
    global can_interface
    can_interface=start_canbus()
    can_Filter()
    Botschaft=canbus_Botschaft_lesen(can_interface)
    B=can_Botschaft_aufteilen(Botschaft)
    print(B)
    print("Beispiel_canbus_init.py wurde ausgefuehrt", Botschaft)

