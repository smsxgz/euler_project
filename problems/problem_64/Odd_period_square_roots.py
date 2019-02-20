import math


def period(n):
    a = int(math.sqrt(n + 0.5))
    if a * a == n:
        return 0
    b, c = a, 1
    pd = 1
    while True:
        tmp_c = n - b * b
        assert tmp_c % c == 0
        c = tmp_c // c
        if c == 1:
            return pd
        b = a - (a + b) % c
        pd += 1


def solve(N=10000):
    res = 0
    for n in range(2, N + 1):
        if period(n) % 2 == 1:
            res += 1
    return res


if __name__ == '__main__':
    solve()
