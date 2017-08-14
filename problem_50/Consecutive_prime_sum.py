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


N = 1000000
prime = euler_prime(N)
psum = [0]
s = 0
j = None
for i, p in enumerate(prime):
    ps = psum[-1] + p
    if ps > N and s == 0:
        j = i
        s = 1
    psum.append(ps)

prime = set(prime)
r = None
while True:
    i = j
    while True:
        q = psum[i] - psum[i - j]
        if q > N:
            break
        if q in prime:
            print(q)
            r = q
            break
        i += 1
    if r:
        break
    j -= 1
