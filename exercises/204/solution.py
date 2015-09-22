# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 10:38:13 2015

@author: MDeyell
"""


def perfect_shuffle(deck):
    shuffle = [0] * len(deck)
    c1 = 0
    if ((len(deck) % 2) == 0):
        c2 = int(len(deck) / 2)
    else:
        c2 = int(len(deck) / 2) + 1
    for i in range(len(deck)):
        if ((i % 2) == 0):
            shuffle[i] = deck[c1]
            c1 = c1 + 1
        else:
            shuffle[i] = deck[c2]
            c2 = c2 + 1
    return shuffle
