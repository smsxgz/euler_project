# -*- coding: utf-8 -*-
from numpy import sqrt, log


def fib(N):
    f = (0, 1)
    s = [(0, 1)]
    idx = 1
    while f[1] < N:
        a, b = f
        f = (a * a + b * b, (2 * a + b) * b)
        idx *= 2
        s.append(f)
    g = s.pop()
    if g[0] < N:
        return idx
    idx = idx // 2
    p = idx
    g = s.pop()
    while True:
        p = p // 2
        f = s.pop()
        h = (g[0] * f[0] + g[1] * f[1], g[1] * f[0] + (g[0] + g[1]) * f[1])
        if h[0] < N and h[1] >= N:
            return idx + p
        if h[1] < N:
            g = h
            idx = idx + p


fib(10**999)

# We can compute it more efficient!!
phi = (1 + sqrt(5)) / 2
(999 * log(10) + log(5) / 2) / log(phi)
