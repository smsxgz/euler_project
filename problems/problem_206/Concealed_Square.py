#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 15:44:56 2017

@author: smsxgz
"""

import math
import time

s = '1_2_3_4_5_6_7_8_9'


n_min = math.ceil(math.sqrt(int(s.replace('_', '0'))))
n_max = math.ceil(math.sqrt(int(s.replace('_', '9'))))


start = time.time()
for i in range(n_min // 10, n_max // 10 + 1):
    k = 10 * i + 3
    m = k**2
    if str(m)[::2] == '123456789':
        break
    k = k + 4
    m = k**2
    if str(m)[::2] == '123456789':
        break
print(time.time() - start)


start = time.time()
k = 10 * (n_min // 10 - 1) + 7
m = k * k
for i in range(n_min // 10, n_max // 10 + 1):
    m = m + 12 * k + 36
    k = k + 6
    if str(m)[::2] == '123456789':
        break
    m = m + 8 * k + 16
    k = k + 4
    if str(m)[::2] == '123456789':
        break
print(time.time() - start)



