from mylib import gcd


def count(x, y, n):
    d = gcd(x, y)
    x1, y1 = x // d, y // d

    res = 0
    x2, y2 = x, y
    while x2 >= y1 and y2 <= n - x1:
        x2 -= y1
        y2 += x1
        res += 1

    x2, y2 = x, y
    while x2 <= n - y1 and y2 >= x1:
        x2 += y1
        y2 -= x1
        res += 1

    return res


def solve(n):
    res = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            res += count(i, j, n)
    res += n * n * 3

    return res


if __name__ == '__main__':
    solve(50)
