#!/usr/bin/python python
# -*- coding: utf-8 -*-

import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


class programm(App):


    title = 'CANbus'
#    icon = 'canbus2.png'
    def build(self):
        # Hintergrundfarbe ist Weis
        Window.clearcolor = (0.1,0.3,0.8,1)
        #groesse des Fenters festlegen
        Window.size = (800, 480)
        #Window.size = (2560,1440)
        # ganzen Bildschirm
        #Window.fullscreen = True


if __name__=="__main__":

    programm().run()