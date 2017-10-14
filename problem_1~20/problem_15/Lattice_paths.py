# -*- coding: utf-8 -*-
from functools import reduce


def mul(x, y):
    return x * y


2 * reduce(mul, range(21, 40)) // reduce(mul, range(2, 20))
