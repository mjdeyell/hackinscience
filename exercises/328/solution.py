# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 10:38:13 2015

@author: MDeyell
"""


def mul(a):
    try:
        out = a[0]
        for i in range(1, len(a)):
            out = out * a[i]
        return (out)
    except Exception:
        return "Invalid input jerk."
