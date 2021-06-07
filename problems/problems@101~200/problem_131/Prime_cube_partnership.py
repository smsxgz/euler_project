from mylib import euler_prime, sqrt

primes = euler_prime(1000000)


def is_square(m):
    sq = sqrt(m)
    return sq**2 == m


def helper(p):
    sq = sqrt((p - 1) // 3)
    for s in range(1, sq + 1):
        t = 4 * p - 3 * s**2
        sqt = sqrt(t)
        if sqt**2 == t and (sqt * s**3 + 3 * s**4) % (2 * (p - 3 * s**2)) == 0:
            return True
    return False


if __name__ == '__main__':
    res = 0
    for p in primes:
        res += helper(p)
    print(res)
