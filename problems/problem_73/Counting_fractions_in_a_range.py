from mylib import sqrt, Mobius, euler_prime, StopWatch


def fraction_less(D, mobius, mul=2):
    """ number of the fractions such that p/q <= 1/mul """
    res = 0
    for d in range(1, D + 1):
        i, r = divmod(D // d, mul)

        s = i * (i + 1) // 2 * mul
        s = s - (mul - 1 - r) * i
        res += mobius[d] * s

    return res


def countSB(limit, left, right):
    count = 0
    top = 0
    stack = [None] * (limit // 2)

    while True:
        med = left + right
        if med > limit:
            if top > 0:
                left = right
                top = top - 1
                right = stack[top]
            else:
                break
        else:
            count += 1
            stack[top] = right
            top += 1
            right = med
    return count


def inclusionExclusion(limit, index, primes):
    q, r = divmod(limit, 6)
    count = q * (3 * q - 2 + r) + (r == 5)
    while index < len(primes) and 5 * primes[index] <= limit:
        newLimit = limit // primes[index]
        count -= inclusionExclusion(newLimit, index + 1, primes)
        index += 1
    return count


def F(n):
    q, r = divmod(n, 6)
    return q * (3 * q - 2 + r) + (r == 5)


def sublinear_solve(N):
    K = sqrt(N // 2)
    M = N // (2 * K + 1)
    rsmall = [0] * (M + 1)
    rlarge = [0] * K

    def R(n):
        switch = sqrt(n // 2)
        count = F(n) - F(n // 2)

        m = 5
        k = (n - 5) // 10
        while k >= switch:
            nextk = (n // (m + 1) - 1) // 2
            count = count - (k - nextk) * rsmall[m]
            k = nextk
            m += 1
        while k > 0:
            m = n // (2 * k + 1)
            if m <= M:
                count -= rsmall[m]
            else:
                count -= rlarge[((N // m) - 1) // 2]

            k -= 1
        if n <= M:
            rsmall[n] = count
        else:
            rlarge[((N // n) - 1) // 2] = count

    for n in range(5, M + 1):
        R(n)
    for j in range(K - 1, -1, -1):
        R(N // (2 * j + 1))

    return rlarge[0]


D = 12000
with StopWatch():
    mobius = Mobius(D)
    print(fraction_less(D, mobius, 2) - fraction_less(D, mobius, 3) - 1)

# with StopWatch():
#     print(countSB(D, 3, 2))

with StopWatch():
    primes = euler_prime(D)
    print(inclusionExclusion(D, 0, primes))

with StopWatch():
    print(sublinear_solve(D))
