# -*- coding: utf-8 -*-
from numpy import sqrt


def num_divisor(n):
    if n % 2 == 0:
        n = n // 2
        j = 2
        while n % 2 == 0:
            n = n // 2
            j += 1
    else:
        j = 1
    factor = 3
    maxFactor = sqrt(n)
    while n > 1 and factor <= maxFactor:
        if n % factor == 0:
            n = n // factor
            i = 2
            while n % factor == 0:
                n = n // factor
                i += 1
            maxFactor = sqrt(n)
            j *= i
        factor = factor + 2
    if n == 1:
        return j
    else:
        return 2 * j


def generator():
    saver = [0, 1, 2]
    l = 2
    i = 0
    while True:
        i += 1
        if i % 2 == 1:
            while i > l:
                l += 1
                saver.append(num_divisor(l))
            yield i, saver[i] * saver[(i + 1) // 2]
        else:
            while i + 1 > l:
                l += 1
                saver.append(num_divisor(l))
            yield i, saver[i + 1] * saver[i // 2]


g = generator()
h = next(g)
while h[1] <= 500:
    h = next(g)
print(h[0] * (h[0] + 1) // 2)
