# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 10:38:13 2015

@author: MDeyell
"""
n = 10
output = [1, 2]
for i in range(2, n):
    x = output[i-2] + output[i-1]
    output.append(x)
print(", ".join(str(e) for e in output) + ".")
