def digits2num(digits):
    res = 0
    for d in digits:
        res = 10 * res + d
    return res


mem = dict()
mem[0] = 0
for n in range(1, 12):
    mem[n] = n * 10**(n-1)


def helper(digits):
    n = len(digits)
    if n == 0:
        return 0

    res = 0
    d = digits[0]
    if d >= 2:
        res += 10 ** (n-1)
    elif d == 1:
        res += digits2num(digits[1:]) + 1

    res += d * mem[n-1] + helper(digits[1:])
    return res


def solve(n, d, c=0, k=-1, prefix=0):
    # f(b, d) + k * b = c, b <= 10^n - 1
    if n == 1:
        if c == 0:
            yield 10 * prefix

        for i in range(1, 10):
            if (i < d and k * i == c) or (i >= d and 1 + k * i == c):
                yield 10 * prefix + i

        return

    if k == -1:
        upper = n * 10**(n-1)
        lower = -10**n + 1
    else:
        upper = n * 10**(n-1) + k * (10**n - 1)
        lower = 0

    if c > upper or c < lower:
        return

    for i in range(10):
        if i < d:
            cc = c - i * (n - 1 + 10 * k) * 10**(n - 2)
            yield from solve(n - 1, d, cc, k, 10 * prefix + i)
        elif i == d:
            cc = c - i * (n - 1 + 10 * k) * 10**(n - 2) - 1
            yield from solve(n - 1, d, cc, k + 1, 10 * prefix + i)
        else:
            cc = c - (10 + i * (n - 1 + 10 * k)) * 10**(n - 2)
            yield from solve(n - 1, d, cc, k, 10 * prefix + i)


if __name__ == '__main__':
    res = 0
    for d in range(1, 10):
        for s in solve(11, d):
            res += s
    print(res)
