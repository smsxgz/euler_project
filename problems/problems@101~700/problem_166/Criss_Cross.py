#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 12:41:52 2017

@author: smsxgz
"""


def is_true(mlist):
    for m in mlist:
        if m > 9 or m < 0:
            return False
    return True


def Criss_Cross(S):
    num = 0
    for n in range(100000):
        l = []
        for i in range(5):
            l = [n % 10] + l
            n = n // 10

        S1 = sum(l[:3])
        if (S1 > S) or (S1 < S - 9):
            continue

        S2 = sum(l[2:])
        if (S2 > S) or (S2 < S - 9):
            continue

        SS = S1 + S2
        S3 = SS - S
        S4 = 2 * S - SS

        S5 = l[2] + S4
        if (S5 > S) or (S5 < S - 9):
            continue

        for a in range(10):
            for b in range(10):
                c = S3 - b
                d = S4 - a
                e = S - (l[1] + a + b)
                f = S - (l[0] + c + d)
                g = S - (l[3] + a + c)
                h = S - (l[4] + b + d)
                if is_true([c, d, e, f, g, h]):
                    num += 1
    return num


result = 0
for i in range(18):
    result += Criss_Cross(i)
print(2 * result + Criss_Cross(18))


