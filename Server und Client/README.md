# Beispiele

Beispiel für die Verwendung von socket für eine TCP Verbindung über IPv4:

    Das Serverbeispiel (server_beispiel.py) zeigt die Möglichkeit
     - empfangene Schlüsselwörter wie DATEN oder AB
     - Schlüsselwort DATEN führt zum senden eines Strings
     - Schlüsselwort Stop stoppt den Server
     - Die Verbindung durch das Senden des Stings AB zu beenden
       der Server läuft weiter und wartet auf die nächste Verbindung
     - Es ist nur ein Verbindung erlaubt
    Befehle:
            socket(), bind(), listen(), accept(),sendall(), recv()


    Das Clientbeispiel (client_beispiel.py) zeigt die Möglichkeit
     - zum Aufbau der Verbindung mit dem Server,
     - das Senden und Empfangen von Daten,
     - sowie das Beenden der Verbindung
     - Steuerung üder die oben beschriebenen Schlüsselwörter
    Befehle:
            socket(), connect(), sendall(), recv()



