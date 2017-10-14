# -*- coding: utf-8 -*-

d = {1: 1}


def Collatz_sequence(i):
    """i is odd"""
    if i in d:
        return d[i]

    i = 3 * i + 1
    j = 1
    while i % 2 == 0:
        j += 1
        i = i // 2

    if i == 1:
        return j + 1
    e = j + Collatz_sequence(i)
    d[i] = e
    return e


I = 0
M = 0
for i in range(1, 1000000, 2):
    e = Collatz_sequence(i)
    if e > M:
        M = e
        I = i
I
