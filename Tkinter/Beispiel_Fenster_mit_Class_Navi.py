import tkinter as tk
from tkinter import ttk

LARGE_FONT= ('Verdana',12)
FENSTER_NAME="CANBUS Ausgabe"

class Fenster(tk.Tk):

    def __init__(self, Beschreibung,*args, **kwargs):
        # erzeugt ein Fenster
        tk.Tk.__init__(self, *args, **kwargs)
        # das Fenster bekommt einen Rahmen mit folgenden Eigenschaften als Standard
        container=tk.Frame(self, borderwidth=5, relief="raised", width=200, height=100)
        container.pack(side='top', fill='both', expand=True)

        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        self.title(Beschreibung)

        # Platzhalter fuer verschiedene Oberflaechen des Fensters
        self.frames={}

        # Liste der verfuegbaren Seiten
        for Seite in (Seite_1_CAN_Werte, Seite_2_Konfiguration,
        Seite_3_Warnmeldung):

            frame=Seite(container,self)

            self.frames[Seite]=frame

            frame.grid(row=0, column=0, sticky='news')

        self.anzeige_oberflaeche(Seite_1_CAN_Werte)


    def anzeige_oberflaeche(self,cont):
        # Der Inhalt von cont ist StartPage2 also das Blatt1
        frame=self.frames[cont]
        frame.tkraise()

class Seite_1_CAN_Werte(tk.Frame,ttk.Style):

    def __init__(self,parent, controller):
        tk.Frame.__init__(self,parent)
        ttk.Style.__init__(self,parent)
        #tk.LabelFrame.__init__(self,parent)
        global Hauptrahmen
        R_Beschreibung="CANBUS-Werte"
        R_Breite=760
        R_Hoehe=350
        SCHRIFT_GROESSE = 15
        SCHRIFT_ART = 'DejaVu Serif'

        Hauptrahmen=tk.LabelFrame(self, text=R_Beschreibung, width=R_Breite,
        height=R_Hoehe, borderwidth=5,highlightthickness=0,
        font=(SCHRIFT_ART,SCHRIFT_GROESSE))

        Hauptrahmen.grid_propagate(False)
        Hauptrahmen.grid(column=0, row=0, columnspan=7 , padx=5, pady=5)

        knopf = tk.Button(self, text="Schliessen", command=self.quit)
        knopf.grid(column=0, row=1)

        knopf = tk.Button(self, text="Konfigurieren",
        command=lambda: controller.anzeige_oberflaeche(Seite_2_Konfiguration))
        knopf.grid(column=6, row=1)

        pass
class Seite_2_Konfiguration(tk.Frame,ttk.Style):

    def __init__(self,parent, controller):
        tk.Frame.__init__(self,parent)

        knopf = tk.Button(self, text="Schliessen", command=self.quit)
        knopf.grid(column=0, row=1)

        knopf2 = tk.Button(self, text="Anzeige der CAN Werte",
        command=lambda: controller.anzeige_oberflaeche(Seite_1_CAN_Werte))
        knopf2.grid(column=6, row=1)

        knopf3 = tk.Button(self, text="Warnmeldung",
        command=lambda: controller.anzeige_oberflaeche(Seite_3_Warnmeldung))
        knopf3.grid(column=3, row=1)
        pass

class Seite_3_Warnmeldung(tk.Frame,ttk.Style):

    def __init__(self,parent, controller):
        tk.Frame.__init__(self,parent)

        knopf = tk.Button(self, text="Schliessen", command=self.quit)
        knopf.grid(column=0, row=1)
        pass


def main():
    ''' Hauptschleife'''

    #Hauptfenster_konfigurieren()
    global MASTER_FENSTER
    MASTER_FENSTER=Fenster(FENSTER_NAME)


    #Hauptfenster=Hauptfenster_erzeugen(MASTER_FENSTER,"CANBUS Ausgabe")

    # CANBUS aktvieren
    # standard filter_id 0x64 bzw. 100
    # filter_id 0x65 kann vorgegeben werden
    # z.B. start_prozedur_canbus(101)

    #start_prozedur_canbus()

    MASTER_FENSTER.mainloop()



if __name__ == '__main__':
    main()
