# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 10:38:13 2015

@author: MDeyell
"""
from string import ascii_lowercase
forward = 1
backward = -1


def caeser_cypher(s, key, method):
    try:
        output_string = []
        input_string = s.split()
        if (key < 26):
            for i in range(len(input_string)):
                for k in range(len(input_string[i])):
                    output