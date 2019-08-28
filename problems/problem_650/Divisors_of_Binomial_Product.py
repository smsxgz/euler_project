from mylib import StopWatch
import numpy as np
import numba as nb


def euler_prime(n):
    prime = []
    vis = [0] * (n + 1)
    for i in range(2, n + 1):
        if not vis[i]:
            prime.append(i)
        for p in prime:
            if i * p > n:
                break
            vis[i * p] = 1
            if (i % p == 0):
                break
    return prime


@nb.njit
def modinv(b, n):
    x0, x1 = 1, 0
    while n:
        (q, n), b = divmod(b, n), n
        x0, x1 = x1, x0 - q * x1
    return x0


@nb.njit
def powermod(n, k, m):
    r = 1
    while k:
        if k & 1:
            r = r * n % m
        k //= 2
        n = n * n % m
    return r


@nb.njit
def factor(n, primes):
    res = []
    for p in primes:
        m = n
        index = 0
        while p <= m:
            m = m // p
            index += m
        res.append(index)
    return res


@nb.njit
def euler650_helper(L, pLst):
    M = 1000000007
    pLen = len(pLst)
    D = np.ones(L + 1, dtype=np.int64)
    D[0] = 0
    for i in range(pLen):
        p = pLst[i]
        myInv = modinv(p - 1, M)
        eSum = 0
        for n in range(p, L + 1):
            a = 0
            m = n
            while m:
                m //= p
                a += m
            e = (n - 1) * a - 2 * eSum
            D[n] *= (powermod(p, e + 1, M) - 1) * myInv % M
            D[n] %= M
            eSum += a
    return np.sum(D) % M


def solve(L):
    pLst = euler_prime(L)
    return euler650_helper(L, pLst)


if __name__ == "__main__":
    with StopWatch():
        print(solve(20000))
