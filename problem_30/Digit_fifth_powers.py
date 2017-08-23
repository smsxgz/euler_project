# -*- coding: utf-8 -*-
l = []
for i in range(2, 300000):
    if i == sum(int(s)**5 for s in str(i)):
        l.append(i)
sum(l)
