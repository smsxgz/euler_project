# -*- coding: utf-8 -*-
from numpy import sqrt
import time


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
    if j == i:
        continue
    try:
        k = d[j]
    except KeyError:
        k = sum_divisor(j) - j
    if k == i:
        s.append(i)
s
sum(s)


def SumOfDivisors(n):
    s = 1
    p = 2
    while p * p <= n and n > 1:
        if n % p == 0:
            j = p * p
            n = n // p
            while n % p == 0:
                j = j * p
                n = n // p
            s = s * (j - 1)
            s = s // (p - 1)
        if p == 2:
            p = 3
        else:
            p = p + 2
    if n > 1:
        s = s * (n + 1)
    return s


start = time.time()
s = 0
for i in range(2, 10000):
    j = SumOfDivisors(i) - i
    if j > i and SumOfDivisors(j) - j == i:
        s += i + j
s
print(time.time() - start)

n = 10000
start = time.time()
divisorsum = [0] * n
for i in range(1, n // 2):
    for j in range(i * 2, n, i):
        divisorsum[j] += i

for i in range(2, 10000):
    j = divisorsum[i]
    if j > i:
        if j >= n:
            k = SumOfDivisors(j)
        else:
            k = divisorsum[j]
        if k == i:
            s += i + j
s
print(time.time() - start)
