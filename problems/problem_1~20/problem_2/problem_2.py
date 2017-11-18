#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 13:26:39 2017

@author: smsxgz
"""


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

print(problem_2(4000000))
