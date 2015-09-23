# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 10:38:13 2015

@author: MDeyell
"""
import math
import numpy as np


def euclidean(a, b):
    o = (sum((a[i] + b[i])**2 for i in range(len(a)) if len(a) == len(b)))**0.5
    return o


def opt_euclidean(a, b):
    output = math.sqrt(math.fsum((math.pow(a[i] + b[i], 2) for i in
                       range(len(a)) if len(a) == len(b))))
    return output


def np_euclidean(a, b):
    output = np.sqrt(np.sum((np.power(a[i] + b[i], 2) for i in
                     range(len(a)) if len(a) == len(b))))
    return output
