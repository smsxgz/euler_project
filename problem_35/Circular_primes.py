# -*- coding: utf-8 -*-
import time


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


start = time.time()
l = [1, 3, 7, 9]
for k in range(2, 7):
    r = []
    s = [1, 3, 7, 9]
    for _ in range(k):
        u = []
        t = []
        for ss in s:
            for ll in l:
                n = 10 * ss + ll
                u.append(n)
                if is_prime(n):
                    t.append(n)
        r.append(t)
        s = u

ans = []
for i, p in enumerate(r):
    an = len(p)
    p_set = set(p)
    base = 10**(i + 1)
    for q in p:
        for _ in range(i + 1):
            q = (q % base) * 10 + q // base
            if q not in p_set:
                an -= 1
                break
    ans.append(an)
ans

4 + sum(ans)
print(time.time() - start)


# From Nayuki
def sqrt(x):
    assert x >= 0
    i = 1
    while i * i <= x:
        i *= 2
    y = 0
    while i > 0:
        if (y + i)**2 <= x:
            y += i
        i //= 2
    return y


def list_primality(n):
    # Sieve of Eratosthenes
    result = [True] * (n + 1)
    result[0] = result[1] = False
    for i in range(sqrt(n) + 1):
        if result[i]:
            for j in range(i * i, len(result), i):
                result[j] = False
    return result


def compute():
    isprime = list_primality(999999)

    def is_circular_prime(n):
        s = str(n)
        return all(isprime[int(s[i:] + s[:i])] for i in range(len(s)))

    ans = sum(1 for i in range(len(isprime)) if is_circular_prime(i))
    return str(ans)


start = time.time()
compute()
print(time.time() - start)
