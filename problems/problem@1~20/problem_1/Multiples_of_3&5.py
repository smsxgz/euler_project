#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 13:26:39 2017

@author: smsxgz
"""


def problem_1(n):
    l = []
    for i in [3, 5, 15]:
        k = (n - 1) // i
        l.append(k * (k + 1) // 2)
    return 3 * l[0] + 5 * l[1] - 15 * l[2]

print(problem_1(1000))





