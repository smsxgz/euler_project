#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 22:40:24 2017

@author: smsxgz
"""

def euler_prime(n):
    prime = []
    vis = [0] * (n + 1)
    #psum = 0
    for i in range(2, n + 1):
        if not vis[i]:
            prime.append(i)
            #psum += i
        for p in prime:
            if i * p > n:
                break
            vis[i * p] = 1
            if(i % p == 0):
                break
    return prime



len(euler_prime(1300000))
euler_prime(2000000)[10000]
