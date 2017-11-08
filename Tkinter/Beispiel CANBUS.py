#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# coding: utf8
# damit es keine Fehlermeldungen durch Sonderzeichen gibt
import tkinter
from tkinter import ttk
from tkinter import *
import socket
import struct
import threading ,sys
import binascii


class CANBUS_Konfiguration():

    def __init__(self,*args,**kwargs):
        self.dateiname="netzwerk.dbc"
        self.Datei_einlesen()

    def Datei_einlesen(self):
        Datei=open(self.dateiname,'r')
        #lines=len(f.readlines())
        Inhalt=Datei.readlines()
        i = 3                       # Startzeile
        Bot_Konf=[]                 # Botschaftskonfiguration
        while i <= (6):
            Bot_Konf.append(Inhalt[i])
            i +=1

        Datei.close
        self.Bot_Konf=Bot_Konf
        self.Zerlegung()
        print (Bot_Konf, Datei.name)

    def Zerlegung(self):
        i=0
        Konf=[]

        while i <= (3):
            A=self.Bot_Konf[i].split("|")
            #['100 ', ' 1  ', ' pmax1 ', ' - ', ' 0.00152587890625 ',
            #                    ' 0  ', ' 0 ', ' 100 ', ' bar ', '\n']
            Konf.append([int(A[0]), int(A[1]), A[2].replace(" ",""), float(A[4]),
            float(A[5]), float(A[6]), float(A[7]), A[8].replace(" ","")])
            i +=1
        #Bot_id = int(A[0])
        #Wert_Nr = int(A[1])
        #Name = A[2].replace(" ","")
        #Faktor = float(A[4])
        #Offset = float(A[5])
        #Min = float(A[6])
        #Max = float(A[7])
        #Einheit = A[8].replace(" ","")
        #B=len(A)
        #print(Konf)

        # reduzieren der Botschafts_ids ,doppelte wurden entfernt
        bot_ids=[Konf[1][0], Konf[2][0], Konf[3][0], Konf[0][0]]
        self.botliste=list(set(bot_ids))
        self.Start_auslesen_der_Botschatsliste()
        print(sorted(bot_ids))
        print (bot_ids)


    def Start_auslesen_der_Botschatsliste(self):
        # Anzahl der Botschafts IDs , -1 weil 0-2
        bot_anzahl=len(self.botliste)-1
        Botschaften=[]
        i=0
        while i <= (bot_anzahl):
            Botschaften.append("bot" +str(i))
            Botschaften[i]=CANBUS(self.botliste[i])
            i +=1




class CANBUS ():
    # Standard Botschafts ID
    Filter_id=0x64

    def __init__(self,filter_id,*args, **kwargs):
        self.filter_id=filter_id
        self.start_canbus()
        pass

    def start_canbus(self):

        self.can_interface = socket.socket(socket.AF_CAN, socket.SOCK_RAW, socket.CAN_RAW)
                # Name der Schnittstelle
        interface = "vcan0"
        try:
            self.can_interface.bind((interface,))
            self.can_Botschaftsfilter()
            print("Verbindung mit vcan0 wurde hergestellt!")

        except OSError:
            # Anzeige der Meldung im Fenster
            print("Warnung verbindung konnte nicht hergestellt werden!")

    def can_Botschaftsfilter(self):
        print(self.filter_id)
            # 0x64 Botschaft
        #id = 0b000001100100
        mask = 0b011111111111
        can_filter_id=self.filter_id
        filter_mask=0x7FF
        #can_interface.setsockopt(socket.SOL_CAN_RAW, socket.CAN_RAW_FILTER,struct.pack("II", filter_id, mask))
        self.can_interface.setsockopt(socket.SOL_CAN_RAW, socket.CAN_RAW_FILTER,struct.pack("II", can_filter_id,filter_mask))
        self.start_can_daemon()

    def start_can_daemon(self):
        '''
            Start des Abfrageprozesses als paralleler Prozess
        '''
        can_lesen = threading.Thread(target=self.__canbus_Botschaft_lesen__)
        can_lesen.daemon = True
        can_lesen.start()

    def __canbus_Botschaft_lesen__(self):
        while True:
            can_pkt = self.can_interface.recv(16)
            self.__can_Botschaft_aufteilen__(can_pkt)

    def __can_Botschaft_aufteilen__(self, can_pkt):
        # 4 Werte a 16 bit
        FMT = "<IB3x2s2s2s2s"
        can_id, length, wert1, wert2, wert3, wert4 = struct.unpack(FMT, can_pkt)
        # Anzahl der Werte in der Botschaft
        Werteanzahl=int(float(length/2))
        daten=[wert1, wert2, wert3, wert4]
        print(can_id, Werteanzahl, wert1, wert2, wert3, wert4)




def main():
    ''' Hauptschleife'''


    # CANBUS aktvieren
    #  standard filter_id 0x64 bzw. 100
    # filter_id 0x65 kann vorgegeben werden
    fenster=Tk()
    CANBUS_Konfiguration()
    #Bot1=CANBUS(0x64)
    #Bot2=CANBUS(0x65)
    #Ausgabe=Datei_einlesen("netzwerk.dbc")
    #global Konfiguration
    #Konfiguration=Zerlegung(Ausgabe[0])

    mainloop()



if __name__ == '__main__':
    main()