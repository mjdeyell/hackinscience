# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 10:38:13 2015

@author: MDeyell
"""


def draw_n_squares(n):
    if (n > 0):
        out_line = "+---" + "+---" * (n - 1) + "+"
        for i in range(1, n + 1):
            out_line = out_line + ("\n|   " + "|   " * (n - 1) + "|")
            out_line = out_line + ("\n+---" + "+---" * (n - 1) + "+")
        return out_line
    else:
        return "Cannot draw less than one square, jerk"
