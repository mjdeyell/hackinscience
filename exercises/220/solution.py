# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 10:38:13 2015

@author: MDeyell
"""
import prime
out = []
for i in range(10000, 10050):
    if prime.is_prime(i) is True:
        out.append(i)
print(", ".join(str(e) for e in out))
