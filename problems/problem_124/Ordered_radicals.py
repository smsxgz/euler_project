# import heapq
from mylib import euler_prime

prime = euler_prime(12000)

largest_prime_factor = dict()


def generator(n):
    cache = [(2, [0])]
    index = 0
    while index < len(cache):
        # print(cache)
        P, pl = cache[index]
        P1 = P * prime[pl[-1] + 1]
        if P1 <= n:
            cache.append((P1, pl + [pl[-1] + 1]))
        P2 = P // prime[pl[-1]] * prime[pl[-1] + 1]
        if P2 <= n:
            cache.append((P2, pl[:-1] + [pl[-1] + 1]))

        index += 1
    cache.sort(key=lambda x: x[0])
    return cache


def count(lst, m):
    if not lst:
        return 1

    res = 0
    p = prime[lst[0]]
    while m > 0:
        res += count(lst[1:], m)
        m //= p
    return res


def count2(lst, m):
    if not lst:
        return [1]

    res = []
    p = prime[lst[0]]
    pp = 1
    while m > 0:
        for P in count2(lst[1:], m):
            res.append(pp * P)
        m //= p
        pp *= p
    return sorted(res)


N = 100000
radicals = generator(10000)
c = 0
for P, pl in radicals:
    cc = count(pl, N // P)
    if c + cc > 10000:
        print(count2(pl, N // P)[10000 - c - 2] * P)
        break
    c += cc
