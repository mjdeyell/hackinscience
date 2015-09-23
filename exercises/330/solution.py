# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 10:38:13 2015

@author: MDeyell
"""
import json


def load_json(path):
    with open(path) as jayson:
        out = json.load(jayson)
    return out
