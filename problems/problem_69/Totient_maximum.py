# -*- coding: utf-8 -*-


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


s = 1
for p in euler_prime(100):
    if s * p > 1000000:
        print(s)
        break
    s *= p
