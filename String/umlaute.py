#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

def umlaute(string):
    '''
    Funktion: unicode Zeichen  (\\x..) werden in ö,ä oder ü übersetzt utf-8
    http://www.utf8-zeichentabelle.de/
    '''

    # \xfc wird ersetzt durch  ü
    wert = re.sub(r'([.*]*)\\xfc', r'ü', str(string))
    wert = re.sub(r'([.*]*)\\xdc', r'Ü', str(wert))
    # \xf6 wird ersetzt durch ö
    wert = re.sub(r'([.*]*)\\xf6', r'ö', str(wert))
    wert = re.sub(r'([.*]*)\\xd6', r'Ö', str(wert))

    # \xe4 wird ersetzt durch ä
    wert = re.sub(r'([.*]*)\\xe4', r'ä', str(wert))
    wert = re.sub(r'([.*]*)\\xc4', r'Ä', str(wert))

    # \df wird ersetzt durch ß
    wert = re.sub(r'([.*]*)\\xdf', r'Ä', str(wert))

    return wert

string="Buchstaben: \\\xfc \\xf6 \xfctwzer  \\xe4 \\xc4 \\xd6 \\xdc \\xdf"

if __name__ == "__main__":
    string_korr=umlaute(string)

    print("Original Anzeige:\t\t", string)
    print("Korrigierte Anzeige:\t", string_korr)