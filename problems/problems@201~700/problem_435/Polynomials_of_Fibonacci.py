#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 14:12:02 2017

@author: smsxgz
"""

n = 10**15

M0 = 1307674368000
M2 = 2048
M3 = 729
M5 = 125
M7 = 49
M11 = 11
M13 = 13

#m1 = M2 * M11 * M13
#m2 = M3 * M5 * M7

m1 = 1
m2 = M0


def fib(n, M):
    '''Returns the tuple (F(n), F(n+1))(mod M).
    '''
    if n == 0:
        return (0, 1)
    else:
        a, b = fib(n // 2, M)
        c = (a * (b * 2 - a)) % M
        d = (a * a + b * b) % M
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, (c + d) % M)


def power(x, n, M):
    '''Returns the number x**n(mod M).
    '''
    if n == 1:
        return x
    else:
        y = power(x, n // 2, M)
        y = y * y % M
        if n % 2 == 0:
            return y
        else:
            return y * x % M


def ext_euclid(a, b):
    if b == 0:
        return 1, 0
    else:
        x, y = ext_euclid(b, a % b)
        x, y = y, (x - (a // b) * y)
        return x, y


def F(n, k, m):
    M = (k * (k + 1) - 1) * m
    a, b = fib(n, M)
    c = power(k, n + 1, M)
    return (-k + b * c + a * c * k) % M


s1 = 0
for k in range(101):
    # print(F(n, k, m1) % (k * (k + 1) - 1))
    s1 = (s1 + F(n, k, m1) // (k * (k + 1) - 1)) % m1

s2 = 0
for k in range(101):
    # print(F(n, k, m2) % (k * (k + 1) - 1))
    s2 = (s2 + F(n, k, m2) // (k * (k + 1) - 1)) % m2

n1, n2 = ext_euclid(m1, m2)
s = s2 * m1 * n1 + s1 * m2 * n2

s = s % M0
print(s)
'''252541322550
'''