def more_digits(n, m):
    """n > m"""
    while m > 0:
        n //= 10
        m //= 10
    return n > 0


def solve():
    res = 0

    a = 1
    b = 0
    for _ in range(1000):
        t = a
        a = 2 * a + b
        b = t
        if more_digits(a + b, a):
            res += 1
    return res


if __name__ == '__main__':
    solve()
