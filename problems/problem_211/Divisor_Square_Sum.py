from mylib import sqrt


def sigma2(n):
    sieveLimit = sqrt(n)
    spf = [2 if i % 2 == 0 else i for i in range(n + 1)]
    for i in range(3, sieveLimit + 1, 2):
        if spf[i] == i:
            for m in range(i * i, n + 1, 2 * i):
                if spf[m] == m:
                    spf[m] = i

    res = 1
    sigma = [0] * (n + 1)
    sigma[1] = 1
    for i in range(2, n + 1):
        p = spf[i]
        q = 1
        factor = 1
        m = i
        while m % p == 0:
            m //= p
            q *= p**2
            factor += q
        sigma[i] = factor * sigma[m]
        if sqrt(sigma[i])**2 == sigma[i]:
            res += i

    return res


print(sigma2(64000000))
