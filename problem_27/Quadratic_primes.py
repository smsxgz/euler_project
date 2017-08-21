# -*- coding: utf-8 -*-
import time


def euler_prime(n):
    prime = []
    vis = [0] * (n + 1)
    for i in range(2, n + 1):
        if not vis[i]:
            prime.append(i)
        for p in prime:
            if i * p > n:
                break
            vis[i * p] = 1
            if (i % p == 0):
                break
    return prime


start = time.time()
prime = set(euler_prime(10000))
s = [(a, b) for a in range(-999, 1000) for b in euler_prime(1000)]

n = 1
while True:
    l = []
    for a, b in s:
        if (n * n + a * n + b) in prime:
            l.append((a, b))
    if len(l) == 0:
        break
    s = l
    if len(l) == 1:
        break
    n += 1

s
print(time.time() - start)
