def euler_func(n):
    phi = [0] * (n + 1)
    phi[1] = 1
    for i in range(2, n + 1):
        if not phi[i]:
            phi[i] = i - 1
            for j in range(i << 1, n + 1, i):
                if not phi[j]:
                    phi[j] = j
                phi[j] = phi[j] // i * (i - 1)
    return phi


def gcd_sum(n):
    phi = euler_func(n)
    res = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            res[j] += i * phi[j // i]
    return sum(res)


euler_func(10000000)

gcd_sum(10)

[0] * (10**11)
