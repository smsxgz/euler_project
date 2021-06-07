#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 18:48:31 2017

@author: smsxgz
"""


def Red_green_and_blue_tiles(n):
    l = [0, 0, 0, 1]

    k = 0
    while k < n:
        s = sum(l[-4:])
        l.append(s)
        k += 1

    return l[-1]


def Red_green_or_blue_tiles(n):
    l2 = [0, 1]
    l3 = [0, 0, 1]
    l4 = [0, 0, 0, 1]

    k = 0
    while k < n:
        l2.append(l2[-2] + l2[-1])
        l3.append(l3[-3] + l3[-1])
        l4.append(l4[-4] + l4[-1])
        k += 1

    return l2[-1] + l3[-1] + l4[-1] - 3


# print(Red_green_and_blue_tiles(50))
print(Red_green_or_blue_tiles(50))
