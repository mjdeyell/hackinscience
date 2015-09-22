# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 10:38:13 2015

@author: MDeyell
"""
import prime
for i in range(222281, 222381):
    x = bin(i)
    s = 0
    for k in range(2, len(x)):
        s = s + int(x[k])
    if prime.is_prime(s) is True:
        print(i)
