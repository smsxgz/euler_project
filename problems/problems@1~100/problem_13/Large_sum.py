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
    for q in data:
        k += int(q.pop())
    result.append(str(k % 10))
    k //= 10

while k > 0:
    result.append(k % 10)
    k //= 10

res = ''
for i in range(10):
    res += str(result[-i - 1])
print(res)
