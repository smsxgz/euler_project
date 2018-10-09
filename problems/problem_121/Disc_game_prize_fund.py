#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 12:34:48 2017

@author: smsxgz
"""

def disc_game(n):
    prob = {0: 0.5, 1: 0.5, }
    if n == 1:
        return prob
    for i in range(2, n + 1):
        pre_prob = prob
        prob = {}
        for j in range(i + 1):
            if j == 0:
                prob[j] = pre_prob[j] * (i / (i + 1))
            elif j == i:
                prob[j] = pre_prob[j - 1] * (1 / (i + 1))
            else:
                prob[j] = pre_prob[j] * (i / (i + 1)) + pre_prob[j - 1] * (1 / (i + 1))
    return prob

d = disc_game(15)
p = 0
for i in range(8, 16):
    p += d[i]
print(1 / p)