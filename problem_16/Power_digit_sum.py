# -*- coding: utf-8 -*-

N = 2**1000
d = 0
while N > 0:
    d += N % 10
    N = N // 10
d
