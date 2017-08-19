# -*- coding: utf-8 -*-
def Champernowne_s_constant(n):
    l = 1
    i = 1
    j = 9
    while n > j:
        l += 1
        i *= 10
        j += i * l * 9
    a = (j - n) // l
    b = (j - n + 1) % l
    return int(str(10 * i - a - 1)[-b])


M = 1
for n in [1, 10, 100, 1000, 10000, 100000, 1000000]:
    M *= Champernowne_s_constant(n)
M
