# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 10:38:13 2015

@author: MDeyell
"""


def select_student(student_list, grade_threshold):
    sl = student_list
    gt = int(grade_threshold)
    good = []
    bad = []

    def getKey(item):
        return item[1]

    for i in range(len(sl)):
        st = sl[i]
        if (st[1] >= gt):
            good.append(st)
        elif (st[1] < gt):
            bad.append(st)

    sort_good = sorted(good, key=getKey, reverse=True)
    sort_bad = sorted(bad, key=getKey)

    return {'Accepted': sort_good,
            'Refused': sort_bad
            }


