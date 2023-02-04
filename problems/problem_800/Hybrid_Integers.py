from numpy import piecewise
from mylib import euler_prime
from math import log2

N = 800800
M = N * log2(N)

m = int(N * log2(N) - 2)
primes = euler_prime(m)


def search(i):
    p = primes[i]
    l, r = i + 1, len(primes) - 1
    while r - l > 1:
        mid = (l + r) // 2
        q = primes[mid]
        if q * log2(p) + p * log2(q) < M:
            l = mid
        else:
            r = mid
    return l - i


def solve():
    res = 0
    for i, p in enumerate(primes):
        q = primes[i + 1]
        if p * log2(q) + q * log2(p) > M:
            break

        res += search(i)
    print(res)


def solve2():
    res = 0

    i, j = 0, len(primes) - 1
    p, q = primes[i], primes[j]
    while i < j:
        if p * log2(q) + q * log2(p) < M:
            res += j - i
            i += 1
            p = primes[i]
        else:
            j -= 1
            q = primes[j]
    print(res)


if __name__ == "__main__":
    from mylib import StopWatch

    with StopWatch():
        solve()

    with StopWatch():
        solve2()
