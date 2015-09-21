# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 10:38:13 2015

@author: MDeyell
"""


def love_meet(input1, input2):
    outvar = list(set(input1).intersection(input2))
    return outvar


def affair_meet(input1, input2, input3):
    meet = list(set(input1).intersection(input2))
    avoid = list(set(meet).difference(input3))
    return avoid
