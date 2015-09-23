# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 10:38:13 2015

@author: MDeyell
"""
import requests

try:
    r = requests.get('http://mdk.fr/ip')
    a = r.text
    print(a.splitlines()[0])
except Exception:
    print('No internet connectivity.')
