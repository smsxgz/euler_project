# -*- coding: utf-8 -*-
from functools import reduce


def mul(x, y):
    return x * y


N = reduce(mul, range(1, 100))
d = 0
while N > 0:
    d += N % 10
    N = N // 10
d
