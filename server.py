#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import sys
from _thread import start_new_thread


def server_starten():

    HOST_IP = "127.0.0.1"
    PORT = 5000

    # Einstellung für die Schnittstelle AF_INET= IPv4, Sock_STREAM = TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as netzwerkschnittstelle:
        # Bei wiederholten Start des Servers kann es zu dieser Fehlermeldung kommen
        # OSError: [Errno 98] Address already in use
        # Abhilfe schafft  das setzen dieses Flags.
        # das SO_REUSEADDR-Flag sagt dem Kernel, einen lokalen Socket im TIME_WAIT-Zustand wiederzuverwenden,
        # ohne darauf zu warten, dass sein natürliches Timeout abläuft
        netzwerkschnittstelle.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        netzwerkschnittstelle.bind((HOST_IP, PORT))
        netzwerkschnittstelle.listen(1)
        print("Warten auf eine Verbindung.")

        # schnittstelle ist ein Objekt zum empfangen und senden von Daten
        # addr ist die Adressen des anderen PC
        schnittstelle, addr = netzwerkschnittstelle.accept()

        with schnittstelle:
            schnittstelle.send(str.encode("Willkommen auf der Wetterstation! \n"))
            print("Verbunden wurde mit: ", str(addr[0]) + ":" + str(addr[1]) + " hergestellt!" )
            while True:
                daten_empfangen = schnittstelle.recv(2048)
                try:
                    daten_senden = "Antwort des Servers: " + daten_empfangen.decode('utf-8')

                # Wenn ein strg-c gesendet wird die Verbindung getrennt
                # der Server läuft aber weiter
                except UnicodeDecodeError:
                    print("Verbindung wurde durch ungültige Zeichen ^C  vom Client geschlossen!")
                    break
                schnittstelle.sendall(str.encode(daten_senden))
                abbruch = str(daten_empfangen.decode('utf-8'))
                if abbruch[0:2] == 'AA':
                    print("Verbindung wurde durch die Aufforderung des Client geschlosssen!")
                    break

                # Schleifenende

            schnittstelle.close()
'''
    # Bindet die Schnittstelle an die Locale IP und Port
    try:
        netzwerkschnittstelle.bind((HOST_IP, PORT))
    except socket.error as msg:
        #print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
        print("Fehlerbeschreibung \n" + str(msg) + "\n Bitte 20s warten!")
        sys.exit()
    pass

    # Startet das Lesen der Schnittstelle
    # Anzahl der gleichzeitig erlaubten Verbindungen in diesnm Fall 2
    netzwerkschnittstelle.listen(2)

    # schnittstelle ist ein Objekt zum empfangen und senden von Daten
    # addr ist die Adressen des anderen PC
    schnittstelle, addr = netzwerkschnittstelle.accept()
    print('Verbunden mit ' + addr[0] + ':' + str(addr[1]))

    start_new_thread(server_funktion, (schnittstelle,))

    #except KeyboardInterrupt as e:
    #    print("HAllo" + str(e))
    #    sys.exit()
'''




# das soll der Server tun
def server_funktion(conn):
    conn.send(str.encode("Willkommen auf der Wetterstation! \n"))
    while True:
        daten_empfangen=conn.recv(2048)
        try:
            daten_senden="Antwort des Servers: " + daten_empfangen.decode('utf-8')

        # Wenn ein strg-c gesendet wird die Verbindung getrennt
        # der Server läuft aber weiter
        except UnicodeDecodeError:
            print("Verbindung wurde durch ungültige Zeichen ^C  vom Client geschlossen!")
            break
        print("Daten:\t",daten_empfangen.decode('utf-8'))
        abbruch=str(daten_empfangen.decode('utf-8'))
        if abbruch[0:2] == 'AA':
            print("Verbindung wurde geschlosssen!")
            break
        if abbruch != 'AB':
            print("Kein Abbruch!")
            print(abbruch)
        conn.sendall(str.encode(daten_senden))

    conn.close()

if __name__ == "__main__":
    try:
        server_starten()

    except KeyboardInterrupt as e:
        print("\tDas Programm wurde beendet." + str(e))
        sys.exit()
    pass
    '''
    while True:
       # wait to accept a connection - blocking call
       # wartet auf die Verbindung
        try:
            conn, addr = netzwerkschnittstelle.accept()
            print('Verbunden mit ' + addr[0] + ':' + str(addr[1]))
            start_new_thread(server_funktion,(conn,))
        
    
    '''