#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 20:59:18 2017

@author: smsxgz
"""

pete_coff = [1] * 4
fill = [0] * 3

for i in range(1, 9):
    pete_coff_fill = fill + pete_coff + fill
    k = 3 * i + 4
    pete_coff_update = [0] * k
    for j in range(k):
        pete_coff_update[j] = sum(pete_coff_fill[j: j + 4])
    pete_coff = pete_coff_update


Colin_coff = [1] * 6
fill = [0] * 5

for i in range(1, 6):
    Colin_coff_fill = fill + Colin_coff + fill
    k = 5 * i + 6
    Colin_coff_update = [0] * k
    for j in range(k):
        Colin_coff_update[j] = sum(Colin_coff_fill[j: j + 6])
    Colin_coff = Colin_coff_update

p = 0
for i in range(9, 37):
    for j in range(6, i):
        p += pete_coff[i - 9] * Colin_coff[j - 6]

print(p / (4**9 * 6**6))