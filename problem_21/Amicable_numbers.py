# -*- coding: utf-8 -*-
from numpy import sqrt


def sum_divisor(n):
    if n % 2 == 0:
        n = n // 2
        j = 2
        while n % 2 == 0:
            n = n // 2
            j *= 2
        j = 2 * j - 1
    else:
        j = 1
    factor = 3
    maxFactor = sqrt(n)
    while n > 1 and factor <= maxFactor:
        if n % factor == 0:
            n = n // factor
            i = factor
            while n % factor == 0:
                n = n // factor
                i *= factor
            maxFactor = sqrt(n)
            j *= (i * factor - 1) // (factor - 1)
        factor = factor + 2
    if n == 1:
        return j
    else:
        return j * (1 + n)


d = {}
for i in range(1, 10000):
    d[i] = sum_divisor(i) - i

s = []
for i in range(2, 10000):
    j = d[i]
    try:
        k = d[j]
    except KeyError:
        k = sum_divisor(j) - j
    if k == i:
        s.append(i)
s
