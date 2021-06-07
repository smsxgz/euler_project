#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 11:30:04 2017

@author: smsxgz
"""


def Counting_block_combinations_1(n):
    flist = [0] * (n + 1)
    glist = [0] * (n + 1)
    flist[0] = 1
    glist[0] = 1

    for i in range(1, n + 1):
        if i < 3:
            glist[i] = 0
        else:
            glist[i] = sum(flist[0:i - 3]) + 1
        flist[i] = sum(glist[0:i + 1])
    return flist[-1]


#  print(Counting_block_combinations_1(50))


def Counting_block_combinations_2(m, n):
    flist = [0] * (n + 1)
    glist = [0] * (n + 1)
    flist[0] = 1
    glist[0] = 1

    for i in range(1, n + 1):
        if i < m:
            glist[i] = 0
        else:
            glist[i] = sum(flist[0:i - m]) + 1
        flist[i] = sum(glist[0:i + 1])
    return flist[-1]


#  print(Counting_block_combinations_2(10, 57))
print(Counting_block_combinations_2(50, 167))
