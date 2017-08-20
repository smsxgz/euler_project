# -*- coding: utf-8 -*-


def Lexicographic_permutations(n):
    l = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    dig = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    s = []
    while True:
        if len(dig) == 0:
            break
        m = l.pop()
        k = n // m
        n = n % m
        s.append(dig[k])
        dig.pop(k)
    return s


s = Lexicographic_permutations(999999)

t = 0
for i in s:
    t = 10 * t + i
t
