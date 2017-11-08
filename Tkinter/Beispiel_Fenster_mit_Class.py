import tkinter as tk

LARGE_FONT= ('Verdana',12)

class Fenster(tk.Tk):

    def __init__(self, *args, **kwargs):

        # erzeugt ein Fenster
        tk.Tk.__init__(self, *args, **kwargs)
        # das Fenster bekommt einen Rahmen mit folgenden Eigenschaften als Standard
        container=tk.Frame(self, borderwidth=5, relief="raised", width=200, height=100)
        container.pack(side='top', fill='both', expand=True)

        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        self.frames={}

        # Aufruf der Class StartPage2
        # Die Klasse besteht aus einem Rahmen und einem Text(Label)
        # Es wird ein Rahmen oder Blatt erzeugt mit dem titel Startseite
        frame=StartPage2(container,self)

        # Dieser Rahmen bzw. Blatt wird dann in self.frames gelegt
        # als Blatt 1 zum Beispiel
        self.frames[StartPage2]=frame

        frame.grid(row=0, column=0, sticky='news')

        self.show_frame(StartPage2)
        '''
        container
            |-- Rahmen(frame)
            |-- Raster(grid)

          self.frames ist ein Platzhalter fuer mehrere Rahmen (Seiten)
          die Aufgerufen werden koennen
        self.frames  (leer)
        z.B. self.frames
                    |-- Startseite
                    |-- Warnmeldung
                    |-- App Fenster
                    |-- Blatt1
                    |-- StartPage2

        self.frames[StartPage]=frame
                |-- Startseite
                        |-- container
                                |-- Rahmen(frame)
                                |-- Raster(grid)
        '''
    def show_frame(self,cont):
        # Der Inhalt von cont ist StartPage2 also das Blatt1
        frame=self.frames[cont]
        frame.tkraise()



class StartPage2(tk.Frame):

    def __init__(self,parent, controller):
        tk.Frame.__init__(self,parent)
        label=tk.Label(self,text='StartSeite',font=LARGE_FONT)
        label.pack(pady=10,padx=10)


app=Fenster()
app.mainloop()