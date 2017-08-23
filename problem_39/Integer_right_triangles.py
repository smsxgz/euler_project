# -*- coding: utf-8 -*-
def gcd(a, b):
    if a < b:
        b, a = a, b
    if b == 0:
        return a
    return gcd(b, a % b)


s = [0] * 1001
for a in range(2, 22):
    k = (500 - a * a) // a
    b = 2 - (a - 1) % 2
    while gcd(a, b) == 1 and b <= k:
        c = 2 * a * a + 2 * a * b
        l = c
        while l <= 1000:
            s[l] += 1
            l += c
        b += 2
        if b > a:
            break

max(enumerate(s), key=lambda x: x[1])
