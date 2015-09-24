# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 10:38:13 2015

@author: MDeyell
"""


def filtered(items, lambda_expression):
    out = []
    for i in range(len(items)):
        if lambda_expression(items[i]):
            out.append(items[i])
    return out


# items = [1, 2, 3, 4, 5, 6]
# even = filtered(items, lambda x: x % 2 == 0)
# odd = filtered(items, lambda x: x % 2 == 1)
# print(even)
# print(odd)

if __name__ == '__main__':
    x1 = filtered(range(1, 100), lambda x: x % 3 == 0)
    print(', '.join(str(e) for e in x1))
    x2 = filtered(range(1, 100), lambda x: x % 5 == 0)
    print(', '.join(str(e) for e in x2))
    x3 = filtered(range(1, 100), lambda x: x % 15 == 0)
    print(', '.join(str(e) for e in x3))
