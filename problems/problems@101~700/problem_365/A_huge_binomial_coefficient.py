from mylib import euler_prime, inverse_mod
from collections import defaultdict

prime = euler_prime(5000)
prime = [p for p in prime if p > 1000]
inverse = defaultdict(dict)
for p in prime:
    for i in range(1, p):
        inverse[p][i] = inverse_mod(i, p)


def residue(n1, n2, p):
    m1 = (n1 - 1) // p + 1
    m2 = n2 // p

    if m2 < m1:
        e = 0
        r = 1
        for i in range(n1, n2 + 1):
            r = r * i % p
    else:
        e, r = residue(m1, m2, p)
        e += m2 - m1 + 1
        if (m2 - m1) % 2 == 1:
            r = p - r
        for i in range(n1, m1 * p):
            r = r * i % p
        for i in range(m2 * p + 1, n2 + 1):
            r = r * i % p
    return e, r


def solve(n, k, p):
    e1, r1 = residue(n - k + 1, n, p)
    e2, r2 = residue(1, k, p)
    if e1 > e2:
        return 0
    else:
        return r1 * inverse[p][r2] % p


def lucas(n, k, p):
    if k == 0:
        return 1
    r = lucas(n // p, k // p, p)
    n, k = n % p, k % p
    for i in range(n - k + 1, n + 1):
        r = r * i % p
    for j in range(2, k + 1):
        r = r * inverse[p][j] % p
    return r


def main(n, k):
    s = len(prime)

    cache = dict()
    for p in prime:
        # cache[p] = solve(n, k, p)
        cache[p] = lucas(n, k, p)

    res = 0
    for i in range(s - 2):
        p = prime[i]
        for j in range(i + 1, s - 1):
            q = prime[j]
            for l in range(j + 1, s):
                r = prime[l]
                mod = p * q * r
                tmp = cache[p] * q * r * inverse[p][q * r % p] % mod
                tmp += cache[q] * r * p * inverse[q][r * p % q] % mod
                tmp += cache[r] * p * q * inverse[r][p * q % r] % mod
                tmp %= mod
                res += tmp
    print(res)


if __name__ == '__main__':
    from mylib import StopWatch

    k = 10**9
    n = k**2
    with StopWatch():
        main(n, k)
