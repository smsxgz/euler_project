from mylib import sqrt
from numba import jit
from numpy import prod


@jit
def Mobius(n):
    prime = [1] * (n + 1)
    mobius = [1] * (n + 1)
    prime_list = []

    for i in range(2, n + 1):
        if not prime[i]:
            continue
        prime_list.append(i)
        mobius[i] = -1
        for j in range(2, n // i + 1):
            prime[i * j] = 0
            mobius[i * j] *= -1
        for j in range(1, n // (i * i) + 1):
            mobius[j * i * i] = 0
    return mobius, prime_list


def square_free(mobius, n):
    s = 0
    for i in range(1, sqrt(n) + 1):
        s += mobius[i] * (n // (i * i))
    return s


def generator(primes, k, N, p0=1):
    if k == 1:
        for p in primes:
            if p * p0 <= N:
                yield [p]
    else:
        for idx, p in enumerate(primes):
            if p0 * prod(primes[idx:idx + k]) > N:
                return
            for lst in generator(primes[idx + 1:], k - 1, N, p0 * p):
                yield [p] + lst


N = 10**16
sqN = sqrt(N)
mobius, prime = Mobius(sqN)
sqN
print(prime[:15])
prod(prime[:9]) > sqN
lth = 0
for lst in generator(prime, 8, sqN):
    lth += 1
print(lth)
