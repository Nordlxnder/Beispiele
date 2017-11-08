#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# coding: utf8
# damit es keine Fehlermeldungen durch Sonderzeichen gibt


a=int("001f",16)
print(a)

b=str(b'\xaa\xad\xba\x11\xaa\xff\xbb\xcc')
W1=b[4:6]+b[8:10]
W2=b[12:14]+b[16:18]
W3=b[20:22]+b[24:26]
W4=b[28:30]+b[32:34]
print (W1,W2,W3,W4)

hex="064"
# Umwandlung von hex in Dezimal bzw. Integer
integer = int(hex, 16)
print("Integer:",integer)
wert=(integer, '0>42b')
print(wert)

# Umwandlung von hex in Binaer
#https://docs.python.org/2/library/string.html#format-specification-mini-language
hex="064"
integer = int(hex, 16)
A=format(integer, '0>12b')
print(A)
hex=0x64
B=format(hex, '0>12b')
print(B)
#'001010101111000001001000111110111111111111'

id = 0x65
mask = 0x7FE
id_B=format(id, '0>12b')
mask_B=format(mask, '0>12b')
print(id_B)
print(mask_B)
print(format((id & mask),'0>12b'))
#t=1234.6564
#a=str(t.zfill(12))

#print(a)
#w=3.14156789
#print('Der Wert von Pi ist ungefähr {0:.4f}.'.format(t))