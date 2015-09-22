# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 10:38:13 2015

@author: MDeyell
"""


def is_multiple(a, b):
    try:
        r = a % b
        if (r == 0):
            out = True
        else:
            out = False
    except ValueError:
        out = False
    return out
