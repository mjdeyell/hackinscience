# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 10:38:13 2015

@author: MDeyell
"""
blah = "abcdefghijklmnopqrstuvwxyz"
for i in range(len(blah)):
    A = blah[i]
    for j in range(len(blah)):
        B = blah[j]
        if (j > i):
            print(A+B)
