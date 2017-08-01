#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 19:57:30 2017

@author: smsxgz
"""

dig_set = set('123456789')

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


def is_unique(m, num_set):
    s = str(m)
    if len(s) > len(set(s) | num_set) - len(num_set):
        return False
    else:
        return True


def Pandigital_prime_sets(prime, num_set = set()):
    if num_set == dig_set:
        return [set()]
    prime = [m for m in prime if is_unique(m, num_set)]
    if prime == []:
        return False
    
    l = []
    for i, p in enumerate(prime):
        set_list = Pandigital_prime_sets(prime[i + 1:], num_set | set(str(p)))
        if set_list:
#            print(set_list)
            for pset in set_list:
                pset.add(p) 
            l = l + set_list
#            print(p)
#            print(set_list)
#            print(l)
    
    if l == []:
        return False
    return l
    


prime = euler_prime(98765432)
#Pandigital_prime_sets(prime[4:], set('2357'))
#set_list = Pandigital_prime_sets(prime)
#print(set_list)



def Pandigital_prime_sets1(prime, num_set = set()):
    if num_set == dig_set:
        return 1
    if prime == []:
        return 0
    
    l = 0
    for i, p in enumerate(prime):
        if is_unique(p, num_set):
            num = Pandigital_prime_sets1(prime[i + 1:], num_set | set(str(p)))
            l += num
        
    return l


print(Pandigital_prime_sets1(prime[4:], set('2357')))
num = Pandigital_prime_sets1(prime)

















