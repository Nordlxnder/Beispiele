#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# coding: utf8
# damit es keine Fehlermeldungen durch Sonderzeichen gibt
import time

#now = time.localtime(time.time())


zeit_letzte=int(time.time()*1000.0)
while 1:
    zeit_akt=int(time.time()*1000.0)
    diff=zeit_akt-zeit_letzte
    if diff >=1000:
        #print (time.ctime(time.time()))
        zeit_letzte=zeit_akt

