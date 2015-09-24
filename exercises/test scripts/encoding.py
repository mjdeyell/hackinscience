# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 14:46:08 2015

@author: MDeyell
"""
from string import ascii_lowercase
forward = 1
backward = -1
ascii_lc = ascii_lowercase
d_ascii = ascii_lowercase + ascii_lowercase

s = 'I @m going to Encode th!s bitch'
key = 7
method = forward

case = s.split()
s_input = s.lower()
o_s = []
i_s = s_input.split()
if (key > 26):
    ukey = key % 26
else:
    ukey = key
for i in range(len(i_s)):
    code = str()
    for k in range(len(i_s[i])):
        try:
            if (ascii_lc.index(i_s[i][k]) >= 0):
                if (i_s[i][k] == case[i][k]):
                    code = (code + d_ascii[ascii_lc.index(i_s[i][k]) +
                            (ukey * method)])
                else:
                    code = (code + d_ascii[ascii_lc.index(i_s[i][k]) +
                            (ukey * method)].upper())
        except Exception:
            code = code + i_s[i][k]
    o_s.append(code)
print(' '.join(str(e) for e in o_s))

if (i_s[0][0] == case[0][0]):
    print('yes')
else:
    test = (d_ascii[ascii_lc.index(i_s[0][0]) + (ukey * method)])
    print(test.upper())
