#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 19:57:30 2017

@author: smsxgz
"""


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


def is_unique(m, num_set=set()):
    s = str(m)
    if len(s) > len(set(s) | num_set) - len(num_set):
        return False
    else:
        return True


dig_set = set('123456789')
prime = euler_prime(98765432)


def Pandigital_prime_sets1(prime, num_set=set()):
    if num_set == dig_set:
        return [set()]
    prime = [m for m in prime if is_unique(m, num_set)]
    if prime == []:
        return False

    l = []
    for i, p in enumerate(prime):
        set_list = Pandigital_prime_sets1(prime[i + 1:], num_set | set(str(p)))
        if set_list:
            for pset in set_list:
                pset.add(p)
            l = l + set_list

    if l == []:
        return False
    return l


def Pandigital_prime_sets2(prime, num_set=set()):
    if num_set == dig_set:
        return 1
    prime = [m for m in prime if is_unique(m, num_set)]
    if prime == []:
        return 0

    l = 0
    for i, p in enumerate(prime):
        if is_unique(p, num_set):
            num = Pandigital_prime_sets2(prime[i + 1:], num_set | set(str(p)))
            l += num

    return l


def sort(s):
    s_list = [t for t in s]
    s_list.sort()
    return ''.join(s_list)


def sub_list(s):
    if len(s) == 1:
        return [s]

    a = s[0]
    l = [a]
    sl = sub_list(s[1:])
    for t in sl:
        l.append(a + t)
    return l + sl


def is_unique1(s1, s2):
    if len(s1) + len(s2) > len(set(s1) | set(s2)):
        return False
    else:
        return True


def Pandigital_prime_sets(prime):
    Pandigital_dict = {}
    sl = sub_list('123456789')
    for s in sl:
        Pandigital_dict[s] = 0

    for p in prime:
        t = sort(str(p))
        if is_unique1('', t) and ('0' not in t):
            Pandigital_dict[t] += 1
            for s in sl:
                if is_unique1(s, t):
                    Pandigital_dict[sort(s + t)] += Pandigital_dict[s]
    return Pandigital_dict


print(Pandigital_prime_sets1(prime[4:], set('2357')))
print(Pandigital_prime_sets2(prime[4:], set('2357')))
# num = Pandigital_prime_sets1(prime)
d = Pandigital_prime_sets(prime)
print(d['123456789'])
