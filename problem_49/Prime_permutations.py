# -*- coding: utf-8 -*-
from collections import Counter


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
prime = [p for p in prime if p > 1000]
prime_str = [''.join(sorted(str(p))) for p in prime]
counter = Counter(prime_str)
for key in counter:
    if counter[key] > 2:
        q = [prime[i] for i in range(len(prime_str)) if prime_str[i] == key]
        m = len(q)
        for i in range(m - 2):
            for j in range(i + 1, m - 1):
                if (2 * q[j] - q[i]) in q:
                    print(q[i], q[j], 2 * q[j] - q[i])
