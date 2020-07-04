# -*- coding: utf-8 -*-
def gcd(a, b):
    if a > b:
        a, b = b, a
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(*args):
    n = len(args)
    if n == 1:
        return args[0]
    a, b, *args = args
    l = a * b // gcd(a, b)
    for k in args:
        l = l * k // gcd(l, k)
    return l


def P(s, N):
    M = lcm(*range(1, (s + 1)))
    m = M
    num = 0
    while m < (N - 1):
        if not m % (s + 1) == 0:
            num += 1
        m += M
    return num


P(6, 10**6)
P(3, 14)
p = 4
s = 0
for i in range(1, 32):
    s += P(i, p)
    p *= 4
s
