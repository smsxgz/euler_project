# -*- coding: utf-8 -*-
def counting(n):
    S = 99
    if n == 1:
        return S

    l = list(range(2, n + 1))
    k = 1
    while k < n:
        for i in range(100 * k + 1, 100 * k + 101):
            if any([i % m == 0 for m in l]):
                S += 1
        l.pop(0)
        k += 1
    return S


counting(6) + counting(4) + 4 * counting(2) + 81 * counting(1)

seen = set(a**b for a in range(2, 101) for b in range(2, 101))
len(seen)
