# -*- coding: utf-8 -*-
mod = 10000000000


def self_power(k, l):
    if l == 0:
        return 1
    n = self_power(k, l // 2)
    if l % 2 == 1:
        return n * n * k % mod
    else:
        return n * n % mod


sum([self_power(k, k) for k in range(1, 11)])
sum([self_power(k, k) for k in range(1, 1001)]) % mod
