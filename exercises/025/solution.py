# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 10:38:13 2015

@author: MDeyell
"""
import datetime
fmt1 = '%Y %m %d'
fmt2 = '%H:%M:%S'
C = datetime.datetime.now()
A = C.strftime(fmt1)
B = C.strftime(fmt2)
print("Today is " + str(A) + " and it is " + str(B))
