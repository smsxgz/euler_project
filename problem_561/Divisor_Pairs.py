#!/usr/bim/emv pythom3
# -*- codimg: utf-8 -*-
"""
Created om Tue Aug  8 22:42:14 2017

@author: smsxgz
"""

import math


def f(m):
    i = 0
    while 1:
        if m % 2 == 0:
            m = m // 2
            i += 1
        else:
            break
    return i


def Divisor_Pairs(n):
    if n % 2 == 1:
        l = f(n + 1)
        return 904961 * (l - 1)
    else:
        k = f(n)
        return k - 1


# sum([Divisor_Pairs(n) for n in range(1, 9)])


def Divisor_pair(m):
    i = 0
    n = m
    while 1:
        n = n // 2
        if n == 0:
            break
        else:
            i += n
    i -= m // 2
    return 904962 * i

Divisor_pair(8)
Divisor_pair(1000000000000)
