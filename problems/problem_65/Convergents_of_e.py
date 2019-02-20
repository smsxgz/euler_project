def digits_sum(n):
    res = 0
    while n > 0:
        n, r = divmod(n, 10)
        res += r
    return res


def solve(iters=100):
    a0, a1 = 2, 3
    b0, b1 = 1, 1
    idx = 3

    while idx <= iters:
        if idx % 3 == 0:
            k = 2 * idx // 3
        else:
            k = 1
        a2 = a1 * k + a0
        a0 = a1
        a1 = a2

        b2 = b1 * k + b0
        b0 = b1
        b1 = b2

        idx += 1

    return digits_sum(a1)


if __name__ == '__main__':
    solve(100)
