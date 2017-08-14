# -*- coding: utf-8 -*-
def palindromes(n, base):
    m = n
    k = 0
    if n % base == 0:
        return False
    while n > 0:
        k = k * base + (n % base)
        n = n // base
    return k == m


S = []
for i in range(1, 10**6):
    if palindromes(i, 10) and palindromes(i, 2):
        S.append(i)
sum(S)
