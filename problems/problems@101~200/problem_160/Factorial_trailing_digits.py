from mylib import inverse_mod, power_mod


def count(n, p):
    res = 0
    while n > 0:
        n //= p
        res += n
    return res


def helper(n, k):
    mod = 5**k

    m = n // mod
    if m % 2 == 0:
        prod = 1
    else:
        prod = -1

    for i in range(1, (n % mod) + 1):
        if i % 5 != 0:
            prod *= i
            prod %= mod

    return prod


def helper2(n, k):
    mod = 5**k
    prod = 1

    for i in range(1, n + 1):
        if i % 5 != 0:
            prod *= i
            prod %= mod

    return prod


def solver(n, k):
    mod = 5**k
    d = count(n, 5)

    f = 1
    while n > 0:
        f *= helper(n, k)
        f %= mod
        n //= 5
    p = inverse_mod(2, mod)
    f *= power_mod(p, d, mod)
    f %= mod

    return f


if __name__ == '__main__':
    f = solver(10**12, 5)
    print(f)
    i = 0
    while True:
        F = f + i * (5**5)
        i += 1
        if F % 32 == 0:
            print(F)
            break
