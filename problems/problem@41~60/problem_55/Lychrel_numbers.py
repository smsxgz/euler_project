def reverse(n):
    reverse = 0
    while n > 0:
        reverse = 10 * reverse + (n % 10)
        n = n // 10
    return reverse


def solve():
    res = 0

    for i in range(5, 10000):
        n = i
        m = reverse(n)
        for _ in range(50):
            n += m
            m = reverse(n)
            if m == n:
                break

        else:
            res += 1

    return res


if __name__ == '__main__':
    solve()
