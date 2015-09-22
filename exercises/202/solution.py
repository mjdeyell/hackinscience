# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 10:38:13 2015

@author: MDeyell
"""


def starts_with(haystack, needle):
    starts = [0] * len(needle)
    out = True
    if (len(haystack) >= len(needle)):
        for i in range(len(needle)):
            if (haystack[i] == needle[i]):
                starts[i] = 1
            else:
                starts[i] = 0
        for i in range(len(starts)):
            if (starts[i] == 0):
                out = False
    else:
        out = False
    return out
