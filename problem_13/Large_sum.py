# -*- coding: utf-8 -*-
from collections import deque

n = 100
m = 50

data = []
with open('data.txt', 'r') as f:
    for line in f.readlines():
        data.append(deque(line.strip(), maxlen=m))

result = []
k = 0
for i in range(m):
    s = k
    for q in data:
        s += int(q.pop())
    k = s // 10
    result.append(str(s % 10))

k
str(k) + ''.join(result[-1:-9:-1])
