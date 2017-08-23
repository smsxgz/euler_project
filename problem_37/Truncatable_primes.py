# -*- coding: utf-8 -*-
def is_prime(p):
    if p == 1:
        return False
    if p == 2:
        return True
    if p == 3:
        return True

    if p % 2 == 0:
        return False
    i = 3
    j = 9
    while j <= p:
        if p % i == 0:
            return False
        i += 2
        j += 4 * i - 4
    return True


l = [1, 3, 7, 9]
s = [2, 3, 5, 7]
ss = []
while True:
    t = []
    for i in s:
        for j in l:
            k = 10 * i + j
            if is_prime(k):
                t.append(k)
    if len(t) == 0:
        break
    s = t
    ss.extend(s)

ss_set = set(ss)
S = []
for p in ss:
    base = 10
    flag = True
    while p > base:
        q = p % base
        if not is_prime(q):
            flag = False
            break
        base *= 10
    if flag:
        S.append(p)
print(S)
len(S)
sum(S)
