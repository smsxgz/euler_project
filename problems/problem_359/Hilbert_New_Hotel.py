def helper(f, r):
    if f == 1:
        a = 1
        n = 2
    else:
        a = f * f // 2
        n = 2 * (f // 2) + 1

    if r % 2 == 0:
        a = n * n - a
        n += 1
        r -= 1
    r = (r - 1) // 2
    a += 2 * r * n + (2 * r - 1) * r

    return a


def main():
    # N = 2**27 * 3 **12
    mod = 10**8

    res = 0
    for i in range(28):
        for j in range(13):
            f = 2**i * 3**j
            r = 2**(27 - i) * 3**(12 - j)
            res += helper(f, r)
            res %= mod
    print(res)


if __name__ == "__main__":
    print(helper(99, 100))
    print(helper(25, 75))
    main()
