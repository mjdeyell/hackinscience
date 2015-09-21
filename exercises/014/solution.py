# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 10:38:13 2015

@author: MDeyell
"""
import sys
file = sys.argv
if len(file) > 1:
    print(file(1))
else:
    print("usage: python3 solution.py PARAM")
