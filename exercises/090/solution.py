# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 10:38:13 2015

@author: MDeyell
"""
import sys
file = sys.argv
l = list(enumerate(file))
for i in range(len(l)):
    temp = l[i]
    print(str(temp[0]) + " " + temp[1])
