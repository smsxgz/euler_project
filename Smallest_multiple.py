#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 18:29:07 2017

@author: smsxgz
"""

import math
p_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]


def Smallest_multiple(n, p_list):
    limit = math.sqrt(n)
    ln = math.log(n)
    a = [1] * len(p_list)
    N = 1
    for i, p in enumerate(p_list):
        if p > n:
            break
        if p <= limit:
            a[i] = math.floor(ln / math.log(p))
        N = N * p ** a[i]
    return N

print(Smallest_multiple(20, p_list))