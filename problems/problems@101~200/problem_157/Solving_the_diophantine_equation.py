from mylib import gcd, sqrt


def num_factors(d):
    f = 1
    if d % 2 == 0:

        while d % 2 == 0:
            d //= 2
            f += 1

    p = 3
    sq = sqrt(d)
    while True:
        if d % p == 0:
            ff = 1
            while d % p == 0:
                d //= p
                ff += 1
            f *= ff
            sq = sqrt(d)

        p += 2
        if sq < p:
            break

    if d > 1:
        f *= 2

    return f


def compute(n):
    factors = []
    for k1 in range(2 * n + 1):
        p1 = 2**k1
        for k2 in range(2 * n + 1):
            factors.append(p1 * 5**k2)
    factors.sort()

    M = 4 * n * (n + 1)
    N = 10**n

    res = 0
    for i in range(M // 2 + 1):
        d = gcd(N + factors[i], N + factors[M - i])
        res += num_factors(d)
    return res


def main():
    res = 0
    for n in range(1, 10):
        res += compute(n)
    print(res)


if __name__ == '__main__':
    main()
