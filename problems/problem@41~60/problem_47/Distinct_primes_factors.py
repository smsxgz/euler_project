# -*- coding: utf-8 -*-
from numpy import sqrt


def Distinct_primes_factors(n):
    if n % 2 == 0:
        num_Factor = 1
        n = n // 2
        while n % 2 == 0:
            n = n // 2
    else:
        num_Factor = 0
    factor = 3
    maxFactor = sqrt(n)
    while n > 1 and factor <= maxFactor:
        if n % factor == 0:
            n = n // factor
            num_Factor += 1
            while n % factor == 0:
                n = n // factor
            maxFactor = sqrt(n)
        factor = factor + 2
    if n == 1:
        return num_Factor
    else:
        return num_Factor + 1


def Generator():
    d = 2
    while True:
        yield d, Distinct_primes_factors(d)
        d += 1


D = Generator()
while True:
    d = next(D)
    if d[1] == 4:
        d = next(D)
        if d[1] == 4:
            d = next(D)
            if d[1] == 4:
                d = next(D)
                if d[1] == 4:
                    print(d[0])
                    break

k = 134046
Distinct_primes_factors(k - 4)
