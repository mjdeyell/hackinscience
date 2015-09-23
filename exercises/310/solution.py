# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 10:38:13 2015

@author: MDeyell
"""

f = open('words.txt', 'r')
a = f.read()
count = 0
for i in range(len(a)):
    if (a[i] == 'e'):
        count = count + 1
print(count)
