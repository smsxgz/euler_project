from math import sqrt


def helper(h):
    return (int(sqrt(4 * h + 4 + 0.5)) - 1) // 2


def count(m, n):
    return m * (m + 1) * n * (n + 1) // 4


def solve():
    N = 2000000
    m = 53
    min_abs = N
    area = None
    while m > 0:
        n = helper(4 * N // (m * (m + 1)))
        k = abs(count(m, n) - N)
        if k < min_abs:
            min_abs = k
            area = m * n

        k = abs(count(m, n + 1) - N)
        if k < min_abs:
            min_abs = k
            area = m * (n + 1)
        m -= 1
    return min_abs, area


if __name__ == '__main__':
    solve()
