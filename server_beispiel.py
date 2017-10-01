#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
    Funktion:   die ist ein Beispiel für einen Server die die empfangenen Daten
                zurück sendet.
                Es wird die locale IP verwendet für Testzwecke
                Für die Verwendung im Netzwerk der Dienst auf der entsprechenden Netzwerkkarte angeboten werden
                Die Verbindung kann durch das senden des String AB beendet werden. Der Server läuft weiter.

'''

import socket
import sys

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

        # das soll der Server tun
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
                # Abruch wenn AB gesendet wird vom client
                if abbruch[0:2] == 'AB':
                    print("Verbindung wurde durch die Aufforderung des Client geschlosssen!")
                    break
            # Schleifenende

            schnittstelle.close()

if __name__ == "__main__":
    try:
        server_starten()
    except KeyboardInterrupt as e:
        print("\tDas Programm wurde beendet." + str(e))
        sys.exit()