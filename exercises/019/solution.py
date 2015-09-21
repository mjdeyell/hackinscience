# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 10:38:13 2015

@author: MDeyell
"""
import sys
file = sys.argv
if len(file) > 2:
    Answer = file(1) + file(2)
    print(Answer)
else:
    print("usage: python3 solution.py OP1 OP2")
