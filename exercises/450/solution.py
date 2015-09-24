# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 10:38:13 2015

@author: MDeyell
"""
from string import ascii_lowercase
forward = 1
backward = -1
double_ascii = ascii_lowercase + ascii_lowercase


def caeser_cypher(s, key, method):
    try:
        s_input = s.lower()
        output_string = []
        input_string = s_input.split()
        if (key < 26):
            for i in range(len(input_string)):
                coded_word = str()
                for k in range(len(input_string[i])):
                    for l in range(len(ascii_lowercase)):
                        if (input_string[i][k] == ascii_lowercase[l]):
                            coded_word = coded_word +\
                                         double_ascii[l + (key * method)]
                output_string.append(coded_word)
        elif (key > 26):
            lower_key = key % 26
            for i in range(len(input_string)):
                coded_word = str()
                for k in range(len(input_string[i])):
                    for l in range(len(ascii_lowercase)):
                        if (input_string[i][k] == ascii_lowercase[l]):
                            coded_word = coded_word +\
                                         double_ascii[l + (lower_key * method)]
                output_string.append(coded_word)
        out_put = ' '.join(str(e) for e in output_string)
        return out_put
    except Exception:
        print('Input error')

# test_input_string = 'Is it I want to encode this string'
# test_output_string = caeser_cypher(test_input_string, 66, forward)
# print(test_output_string)
# test_decode_string = caeser_cypher(test_output_string, 66, backward)
# print(test_decode_string)
