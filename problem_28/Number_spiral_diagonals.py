# -*- coding: utf-8 -*-

x = 1
s = 1
j = 2
while j < 1001:
    for i in range(4):
        x += j
        s += x
    j += 2

s
