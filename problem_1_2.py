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

#print(problem_1(1000))


##########################################
def problem_2(n):
    f0 = 1
    f1 = 1
    f2 = 2
    even_sum = 2
    while(1):
        f0 = f1 + f2
        f1 = f2 + f0
        f2 = f0 + f1
        if f2 > n:
            break
        even_sum += f2
    return even_sum

#print(problem_2(4000000))


