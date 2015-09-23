# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 10:38:13 2015

@author: MDeyell
"""
import sys

try:
    print(sys.argv[1])
except IndexError:
    print("Not enough parameters")
