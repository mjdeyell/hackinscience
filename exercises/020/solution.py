# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 10:38:13 2015

@author: MDeyell
"""
import sys
file = sys.argv
if len(file) > 2:
    A = file[1]
    B = file[2]
    Answer = int(A) - int(B)
    print(Answer)
else:
    print("usage: python3 solution.py OP1 OP2")
