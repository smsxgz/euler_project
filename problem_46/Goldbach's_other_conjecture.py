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


prime = euler_prime(10000)
vis = [0] * 5000
for p in prime[1:]:
    m = p
    d = 1
    while m < 10000:
        vis[m // 2 - 1] = 1
        m = p + 2 * d * d
        d += 1
2 * (vis.index(0) + 1) + 1
