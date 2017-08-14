# -*- coding: utf-8 -*-
num_set = set(range(10))


def search(args):
    S = []
    l = len(args)
    s = num_set - set(args)
    if l == 7:
        i = (2 * args[-2] + 7 * args[-1]) % 17
        if i in s:
            return [args + [i]]
        else:
            return []
    elif l == 6:
        i = (4 * args[-2] + 3 * args[-1]) % 13
        if i in s:
            S += search(args + [i])
        return S
    elif l == 5:
        i = (-args[-2] + args[-1]) % 11
        if i in s:
            S += search(args + [i])
        return S
    elif l == 4:
        i = (-2 * args[-2] - 3 * args[-1]) % 7
        for j in (i, i + 7):
            if j in s:
                S += search(args + [j])
        return S
    elif l == 3:
        for j in (0, 5):
            if j in s:
                S += search(args + [j])
        return S
    elif l == 2:
        i = (-args[-2] - args[-1]) % 3
        for j in (i, i + 3, i + 6, i + 9):
            if j in s:
                S += search(args + [j])
        return S
    elif l == 1:
        for j in (0, 2, 4, 6, 8):
            if j in s:
                S += search(args + [j])
        return S
    elif l == 0:
        for j in range(10):
            if j in s:
                S += search(args + [j])
        return S


S = search([])
N = 0
for args in S:
    n = 0
    for i in args:
        n = n * 10 + i
    s = num_set - set(args)
    a, b = list(s)
    N += (10**8 * 11) * (a + b) + 2 * n
N
