#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 10:53:59 2017

@author: smsxgz
"""


num = [1, 2, 5, 7, 12, 15, 22, 26, 35, 40, 51, 57, 
       70, 77, 92, 100, 117, 126, 145, 155]
c = [1, 1, -1, -1, 1, 1, -1, -1, 1, 1, 
     -1, -1, 1, 1, -1, -1, 1, 1, -1, -1]

def Partitions(n):
    Partition_list = [1]
    for i in range(1, n + 1):
        j = 0
        part = 0
        while(i >= num[j]):
            part += c[j] * Partition_list[i - num[j]]
            j += 1
        Partition_list.append(part)
    return Partition_list


def func(k, l, part):
    p = part[k] * part[l]
    for i in range(k):
        for j in range(l):
            p += part[i] * part[j]
    return p


part = Partitions(60)
print(func(2, 3, part))




'''
t = int(input())
kmax = -1
l = []
for i in range(t):
    m, n = input().split()
    m, n = int(m), int(n)
    kmax = max(kmax, m, n)
    l.append([m ,n])

part = Partitions(kmax)

for m, n in l:
    print(func(m, n, part))
'''