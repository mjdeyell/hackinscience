# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 10:38:13 2015

@author: MDeyell
"""
import sys
"usage: ./solution.py a_number (an_operator +-*/%^) a_number"
if (len(sys.argv) == 4):
    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[3])
        op = str(sys.argv[2])
        operators = ['+', '-', '*', '/', '%', '^']
        if (op == '+'):
            print(num1 + num2)
        elif (op == '-'):
            print(num1 - num2)
        elif (op == '*'):
            print(num1 * num2)
        elif (op == '/'):
            if (num2 == 0):
                print('input error')
            else:
                print(num1 / num2)
        elif (op == '%'):
            if (num2 == 0):
                print('input error')
            else:
                print(num1 % num2)
        elif (op == '^'):
            print(num1 ** num2)
        else:
            print('input error')
    except ValueError:
        print('input error')


else:
    print('usage: ./solution.py a_number (an_operator +-*/%^) a_number')
