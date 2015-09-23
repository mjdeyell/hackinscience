# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 10:38:13 2015

@author: MDeyell
"""

f = open('words.txt', 'r')
a = f.read()
b = {}

for i in range(len(a)):
    try:
        b[a[i]] = b[a[i]] + 1
    except Exception:
        b[a[i]] = 1

del b['\n']

for k in b:
    c = b[k]/len(a)
    print(k + ':', "%.2f" % round(c, 2))
