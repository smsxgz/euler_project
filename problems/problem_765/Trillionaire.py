from fractions import Fraction

p = Fraction(3, 5)

binomial = dict()
for n in range(1, 1001):
    binomial[(n, n)] = 1
    binomial[(n, 0)] = 1
    for i in range(1, n):
        binomial[(n, i)] = binomial[(n - 1, i - 1)] + binomial[(n - 1, i)]


def helper(n, x):
    t = int(2**n / x)
    i = 0
    res = 0
    while t > 0:
        b = binomial[(n, i)]
        if t > b:
            res += b * p**(n - i) * (1 - p)**i
            t -= b
            i += 1
        else:
            res += t * p**(n - i) * (1 - p)**i
            t = 0
            i += 1
    print(float(res))
    # return float(res)
    return res


if __name__ == "__main__":
    print(helper(1000, Fraction(10**12)))
