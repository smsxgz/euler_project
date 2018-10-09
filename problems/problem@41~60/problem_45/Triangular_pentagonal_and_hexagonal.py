# -*- coding: utf-8 -*-


def Generator(k):
    t = 0
    d = 0
    while True:
        t += (k - 2) * d + 1
        d += 1
        yield t


Triangular = Generator(3)
Pentagonal = Generator(5)
Hexagonal = Generator(6)

h = next(Triangular)
p = next(Pentagonal)
t = next(Hexagonal)

for _ in [0, 1]:
    while True:
        h = next(Hexagonal)
        while p < h:
            p = next(Pentagonal)
        while t < h:
            t = next(Triangular)
        if p == h and t == h:
            print(h)
            break
