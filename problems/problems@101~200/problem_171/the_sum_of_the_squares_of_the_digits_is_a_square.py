from math import factorial
from mylib import sqrt


def solve(n, d, c=[1, 4, 9, 16, 25, 36, 49, 64, 81], s=[]):

    t = sum(s)
    if t > d:
        return

    if len(c) == 0:
        if n == 0:
            yield [d - t] + s
        return

    m = c[-1]
    if (d - t) * m < n:
        return

    for i in range(n // m + 1):
        yield from solve(n - i * m, d, c[:-1], [i] + s)


def main(d):
    sq = sqrt(81 * d)
    res = 0

    for i in range(1, sq + 1):
        for solution in solve(i * i, d):
            p = factorial(d)
            q = 0
            for j, s in enumerate(solution):
                p //= factorial(s)
                q += j * s
            res += (p * q // d) * 111111111
            res %= 1000000000
    print(res)


if __name__ == "__main__":
    main(20)
