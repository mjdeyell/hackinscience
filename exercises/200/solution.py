# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 10:38:13 2015

@author: MDeyell
"""


def is_prime(number):
    testset = range(1, int(number**0.5)+1)
    prime = 0
    for i in range(len(testset)):
        p = number % testset[i]
        if (p == 0):
            prime = prime + 1
    if (prime == 1):
        return 'True'
    elif (prime > 1):
        return 'False'
    else:
        return 'Error'
