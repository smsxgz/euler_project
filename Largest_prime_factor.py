    #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 18:50:38 2017

@author: smsxgz
"""

import math

def Largest_prime_factor1(n):
    while(n % 2 == 0):
        n = n // 2
    if n == 1:
        return 2
    p = 3
    while(n > 1):
        while(1):
            if n % p != 0:
                break
            n = n // p
        p += 2
    return p - 2

#print(Largest_prime_factor1(64 * 9))


def Largest_prime_factor(n):
    if n % 2 == 0:
        lastFactor = 2
        n = n // 2
        while n % 2 == 0:
            n = n // 2
    else:
        lastFactor = 1
    factor = 3
    maxFactor = math.sqrt(n)
    while n > 1 and factor <= maxFactor:
        if n % factor == 0:
            n = n // factor
            lastFactor = factor
            while n % factor == 0:
                n = n // factor
            maxFactor = math.sqrt(n)
        factor = factor + 2
    if n == 1:
        return lastFactor
    else:
        return n

print(Largest_prime_factor(18))
