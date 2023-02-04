from mylib import power_mod

N = 1000000007


def binom(n):
    res = dict()
    for m in range(n + 1):
        res[(m, 0)] = 1
        res[(m, m)] = 1

    for m in range(2, n + 1):
        for k in range(1, m):
            res[(m, k)] = res[(m - 1, k - 1)] + res[(m - 1, k)]
            res[(m, k)] = res[(m, k)] % N

    return res


def helper(n=10, binoms=None):

    res = 0
    for m in range(n // 2 + 1, n):
        res += binoms[(n - 1, m)] * power_mod(9, n - m, N)
    res *= 10

    res += binoms[(n - 1, n // 2)] * power_mod(9, n - n // 2, N)
    return res % N


def main(n=10):
    binoms = binom(n)
    res = 9
    for m in range(2, n + 1):
        res += helper(m, binoms)
    print(res % N)


def main2(n=10):
    binoms = binom(n + 1)
    res = 0
    for m in range((n + 1) // 2):
        res += power_mod(9, m + 1, N) * (
            binoms[(n + 1, m + 1)] - binoms[(2 * m + 1, m + 1)]
        )
        res %= N
    print(res % N)


if __name__ == "__main__":
    main(2022)
    main2(2022)
