from mylib import euler_prime

N = 10**18
prime = euler_prime(int((N + 0.5)**(1 / 3)))


def search():
    cache = [
        ([(0, 3)], 8),
    ]

    res = 0
    while cache:
        num, n = cache.pop(0)
        res += N // n

        i, j = num[-1]
        p = prime[i]

        if n * p <= N:
            tmp = num.copy()
            tmp[-1] = (i, j + 1)
            cache.append((tmp, n * p))

        if len(prime) == i + 1:
            continue
        q = prime[i + 1]

        if n * (q**3) <= N:
            tmp = num.copy()
            tmp.append((i + 1, 3))
            cache.append((tmp, n * (q**3)))

        if j == 3:
            tmp_n = n // (p**3) * (q**3)
            if tmp_n <= N:
                tmp = num.copy()
                tmp[-1] = (i + 1, 3)
                cache.append((tmp, tmp_n))

    print(res + N)
    return res


if __name__ == '__main__':
    search()
