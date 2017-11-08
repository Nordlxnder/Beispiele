#!/usr/bin/env python
# -*- coding: utf-8 -*

import threading
from queue import Queue
import time

exitFlag = 0



class sensoren (threading.Thread):
   def __init__(self, name):
      threading.Thread.__init__(self)
      self.name = name

   def run(self):
      print ("Starting " + self.name)
      #print_time(self.name, self.counter, 5)
      sensoren_auslesen()
      print ("Exiting " + self.name)

class server_starten(threading.Thread):
   def __init__(self, name):
      threading.Thread.__init__(self)
      self.name = name

   def run(self):
      print ("Starting " + self.name)
      #print_time(self.name, self.counter, 5)
      server2()
      print ("Exiting " + self.name)

def sensoren_auslesen():
    print("Sensor 1 wird ausgelesen!")
    time.sleep(2)
    print("Sensor2 wird aus gelesen")
    pass

def server2():
   print("Server wird gestartet")
   time.sleep(0.5)
   print("server ist gestartet")
   time.sleep(1)
   pass



# Erzeugt die Jobs die parallel abgearbeitet werden sollen
# thread 1
sensordaten = sensoren("Sensoren")
# thread2
server = server_starten("Server")

# daemon setzen damit die Threads auch beendet werden wenn das Hauptprogramm geschlossen wird
# Vorsicht bei Schreibzugriffen auf eine Datei das kann die Datei beschädigen
sensordaten.daemon=True
server.daemon=True

# Start der neuen Threads
sensordaten.start()
server.start()
sensordaten.join()
server.join()


if __name__ == "__main__":
    pass