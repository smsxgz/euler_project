import numpy as np
from mylib import inverse_mod, euler_prime


N = 300000
primes = euler_prime(N)
print(len(primes))


def helper():
    res = set()

    P = 2
    A = 1
    for i, p in enumerate(primes[1:], start=2):
        a = (i - A) % p
        A += a * inverse_mod(P % p, p) * P
        P *= p
        A %= P

        for q in primes[i:]:
            if A % q == 0:
                res.add(q)

        if i % 1000 == 0:
            print(i, p)
    print(sum(res))


def helper2():
    P = np.array(primes, dtype="int64")
    M = np.ones_like(P)
    X = np.zeros_like(P)
    B = np.zeros(len(P), dtype="bool")

    for i, p in enumerate(P):
        k = (i + 1 - X[i]) * inverse_mod(M[i], p) % p
        X[i:] += k * M[i:]
        X[i:] %= P[i:]
        B[i:][np.logical_not(X[i:])] |= True
        M[i:] *= p
        M[i:] %= P[i:]

    print(np.sum(P[B]))


if __name__ == "__main__":
    helper2()
