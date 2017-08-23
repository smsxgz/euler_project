# -*- coding: utf-8 -*-
import time
from functools import reduce


# Stupid Method !!!
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
prime = euler_prime(87654321)[::-1]
l = []
for p in prime:
    p = str(p)
    s = set([int(s) for s in p])
    if len(s) == len(p):
        if s == set(list(range(1, len(p) + 1))):
            print(p)
            break
print(time.time() - start)


# Better method for problem
def is_prime(p):
    if p == 1:
        return False
    if p == 2:
        return True
    if p == 3:
        return True

    if p % 2 == 0:
        return False
    i = 3
    j = 9
    while j < p:
        if p % i == 0:
            return False
        i += 2
        j += 4 * i - 4
    return True


def permutation(n):
    d = {}
    l = [[1]]
    d[1] = l
    if n == 1:
        return d
    for i in range(2, n + 1):
        s = []
        for j in range(i):
            for ll in l:
                s.append(ll[:j] + [i] + ll[j:])
        d[i] = s
        l = s
    return d


def list_to_num(l):
    return reduce(lambda x, y: 10 * x + y, l)


start = time.time()
s = []
d = permutation(8)
j = 8
while True:
    for l in d[j]:
        m = list_to_num(l)
        if is_prime(m):
            s.append(m)
    if len(s) == 0:
        j -= 1
    else:
        print(max(s))
        break
print(time.time() - start)


def permutation1(dig_list):
    n = len(dig_list)
    if n == 1:
        m = dig_list[0]
        if m in [1, 3, 7]:
            return [[m]]
        else:
            return []
    l = []
    for i in range(n):
        j = dig_list[i]
        for ll in permutation1(dig_list[:i] + dig_list[i + 1:]):
            l.append([j] + ll)
    return l


start = time.time()
s = []
d = permutation1([8, 7, 6, 5, 4, 3, 2, 1])
j = 8
dd = []
flag = False
while True:
    for l in d:
        m = list_to_num(l)
        if is_prime(m):
            print(m)
            flag = True
            break
        if l[0] == j:
            dd.append(l[1:])
    if flag:
        break
    d = dd
    j -= 1
print(time.time() - start)


def permutation2(dig_list):
    n = len(dig_list)
    if n == 1:
        m = dig_list[0]
        if m in [1, 3, 7]:
            return [m]
        else:
            return []
    l = []
    k = 10**(n - 1)
    for i in range(n):
        j = dig_list[i]
        for ll in permutation2(dig_list[:i] + dig_list[i + 1:]):
            l.append(j * k + ll)
    return l


start = time.time()
s = []
d = permutation2([8, 7, 6, 5, 4, 3, 2, 1])
j = 8
p = 10**7
dd = []
flag = False
while True:
    for m in d:
        if is_prime(m):
            print(m)
            flag = True
            break
        if m // p == j:
            dd.append(m % p)
    if flag:
        break
    d = dd
    j -= 1
    p //= 10
print(time.time() - start)
