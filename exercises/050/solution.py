# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 10:38:13 2015

@author: MDeyell
"""
A = 0
for i in range(1, 1001):
    if (i % 3 == 0):
        A = A + i
    elif (i % 5 == 0):
        A = A + i
print(A)
