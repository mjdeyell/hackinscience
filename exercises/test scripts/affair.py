# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 18:08:09 2015

@author: MDeyell
"""
input1 = ['II', 'IV', 'II', 'XIX', 'XV', 'IV', 'II']
input3 = ['IV', 'III', 'II', 'XX', 'II', 'XX']
input2 = ['XVIII', 'XIX', 'III', 'I', 'III', 'XVIII']

meet = set(input1).intersection(input2)
avoid = set(meet).difference(input3)
