# -*- coding: utf-8 -*-
import time


def SumOfDivisors(n):
    s = 1
    p = 2
    while p * p <= n and n > 1:
        if n % p == 0:
            j = p * p
            n = n // p
            while n % p == 0:
                j = j * p
                n = n // p
            s = s * (j - 1)
            s = s // (p - 1)
        if p == 2:
            p = 3
        else:
            p = p + 2
    if n > 1:
        s = s * (n + 1)
    return s


n = 28124

# method 1 to find all abundant numbers
start = time.time()
abundant_list = []
for i in range(2, n):
    if SumOfDivisors(i) > 2 * i:
        abundant_list.append(i)
print(time.time() - start)

# method 2 to find all abundant numbers
start = time.time()
divisorsum = [0] * n
for i in range(1, n // 2):
    for j in range(i * 2, n, i):
        divisorsum[j] += i
abundantnums = [i for (i, x) in enumerate(divisorsum) if x > i]
print(time.time() - start)

L = len(abundant_list)
abundantnums == abundant_list

# method 1
start = time.time()
S = set(list(range(1, n)))
for i in range(L):
    m1 = abundant_list[i]
    for j in range(i, L):
        m = m1 + abundant_list[j]
        if m >= n:
            break
        try:
            S.remove(m)
        except KeyError:
            pass
sum(S)
print(time.time() - start)

# method 2
start = time.time()
expressible = [False] * n
for i in abundant_list:
    for j in abundant_list:
        if i + j < n:
            expressible[i + j] = True
        else:
            break

ans = sum(i for (i, x) in enumerate(expressible) if not x)
ans
print(time.time() - start)
