#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 20:39:32 2017

@author: smsxgz
"""

import math


def gcd(n, m):
    if n == 0:
        return m
    return gcd(m % n, n)


def S(n):
    up1 = math.floor(math.sqrt(n))
    up2 = math.floor(math.sqrt(math.sqrt(n)))

    l = []
    for i in range(1, up2 + 2):
        for j in range(i, up2 + 2):
            if (i + j) * j > (up1 + 1):
                break
            else:
                if gcd(i, j) == 1:
                    l.append((i, j))
    #print(l)
    S = 0
    for i, j in l:
        p = ((i + j) * i)**2
        q = ((i + j) * j)**2
        r = (i * j)**2
        k = math.floor(n / q)
        S += int((p + q + r) * k * (k + 1) / 2)
    return S


print(S(1e9))
