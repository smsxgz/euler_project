# -*- coding: utf-8 -*-
import time

d = {0: 1}
f = 1
for i in range(1, 10):
    f *= i
    d[i] = f
6 * d[9] + d[2]

start = time.time()
l = []
for i in range(3, 6 * d[9] + d[2] + 1):
    if i == sum([d[int(s)] for s in str(i)]):
        l.append(i)
sum(l)
print(time.time() - start)
