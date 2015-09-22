# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 10:38:13 2015

@author: MDeyell
"""


def is_alpha(input_string):
    letterlist = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    Are_letters = [0] * len(input_string)
    All_letters = True
    for i in range(len(input_string)):
        for k in range(len(letterlist)):
            if (input_string[i] == letterlist[k]):
                Are_letters[i] = 1
    for i in range(len(Are_letters)):
        if (Are_letters[i] == 0):
            All_letters = False
    return All_letters
