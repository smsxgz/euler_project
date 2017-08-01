#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 18:52:48 2017

@author: smsxgz
"""

def Partitions(n):
    l = []
    labels = []
    j = 1
    while 1:
        k = (3 * j * j + j) // 2
        l.append(k - j)
        l.append(k)
        label = 1 if j % 2 == 1 else -1
        labels += [label, label]
        if k > n:
            break
        j += 1
    
    
    part_list = [0] * (n + 1)
    part_list[0] = 1
    for i in range(1, n + 1):
        re = 0
        j = 0
        while l[j] <= i:
            re += labels[j] * part_list[i - l[j]]
            j += 1
        part_list[i] = re
        
    return part_list#[-1]

part_list = Partitions(100000)
for i, num in enumerate(part_list):
    if num % 1000000 == 0:
        print(i)