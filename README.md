# Beispiele

Beispiel für die Verwendung von socket:

    Das Serverbeispiel (server_beispiel.py) zeigt die Möglichkeit
     - empfangene Daten zurück zu senden
     - Die Verbindung durch das Senden des Stings AB zu beenden
       der Server läuft weiter und wartet auf die nächste Verbindung
     - Es ist nur ein Verbindung erlaubt
    Befehle:
            socket(), bind(), listen(), accept(),sendall(), recv()




    Das Clientbeispiel (client_beispiel.py) zeigt die Möglichkeit
     - zum Aufbau der Verbindung mit dem Server,
     - das Senden und Empfangen von Daten,
     - sowie das Beenden der Verbindung
    Befehle:
            socket(), connect(), sendall(), recv()



