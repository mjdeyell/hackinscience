# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 10:38:13 2015

@author: MDeyell
"""
import prime

prime_sum = 0
for i in range(1000):
    if prime.is_prime(i) is True:
        prime_sum = prime_sum + i
print(prime_sum)
