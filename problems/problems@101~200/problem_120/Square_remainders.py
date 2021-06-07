#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 21:11:30 2017

@author: smsxgz
"""


s = 0
for a in range(3, 1001):
    s += 2 * ((a + 1) // 2 - 1) * a
print(s)