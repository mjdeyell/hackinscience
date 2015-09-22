# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 10:38:13 2015

@author: MDeyell
"""
import prime
import itertools

n = 100000000
for i in itertools.count(n):
    if prime.is_prime(i) is True:
        print(i)
        break
