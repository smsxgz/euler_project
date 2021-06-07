import math


def inverfc(x):
    t = math.sqrt(math.pi) / 2 * (1 - x)
    return (((127 / 21 * t**2 + 7) * t**2 / 10 + 1) * t**2 / 3 + 1) * t


def solve(eta):
    # \eta = \lambda - 1 - \ln\lambda
    lam = 1.5

    def f(z):
        return z - 1 - math.log(z) - eta

    def g(z):
        return 1 - 1 / z

    while f(lam) > 1e-6:
        lam -= f(lam) / g(lam)

    return lam


def approximation1(n=100):
    eta0 = inverfc(0.5)**2 / n
    lam0 = solve(eta0)
    return lam0 * n


def log_gamma(x, n=100):
    res = -x + (n - 1) * (math.log(x / (n - 1)) + 1) - math.log(2 * math.pi *
                                                                (n - 1)) / 2
    a = 1.0
    s = 0.0
    for i in range(1, n):
        s += a
        a *= (n - i) / x
        if a < 1e-20:
            break
    return res + math.log(s)


def approximation2(n=100):
    approx = approximation1(n)
    m = n // 10
    lo = approx // m * m
    hi = (approx // m + 1) * m

    while hi - lo > 5e-3:
        mid = (hi + lo) / 2
        if log_gamma(mid, n) + math.log(4) > 0:
            lo = mid
        else:
            hi = mid
    return lo


if __name__ == "__main__":
    print(approximation2(10000000) / math.log(10))
