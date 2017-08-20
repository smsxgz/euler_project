# -*- coding: utf-8 -*-
import time


def palindrome(n, base):
    m = n
    k = 0
    if n % base == 0:
        return False
    while n > 0:
        k = k * base + (n % base)
        n = n // base
    return k == m


start = time.time()
S = 0
for i in range(1, 10**6):
    if palindrome(i, 10) and palindrome(i, 2):
        S += i
print(time.time() - start)
print(S)


def makePalindromeBase2(n, oddlength):
    res = n
    if oddlength:
        n = n >> 1
    while n > 0:
        res = (res << 1) + (n & 1)
        n = n >> 1
    return res


start = time.time()
limit = 1000000
S = 0
i = 1
p = makePalindromeBase2(i, True)
while p < limit:
    if palindrome(p, 10):
        S = S + p
    i = i + 1
    p = makePalindromeBase2(i, True)

i = 1
p = makePalindromeBase2(i, False)
while p < limit:
    if palindrome(p, 10):
        S = S + p
    i = i + 1
    p = makePalindromeBase2(i, False)
print(time.time() - start)
print(S)
