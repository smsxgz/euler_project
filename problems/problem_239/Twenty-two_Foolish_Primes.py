def binomial_coefficient(n):
    c = [1]
    for i in range(1, n + 1):
        newc = [1]
        for j in range(i - 1):
            newc.append(c[j] + c[j + 1])
        newc.append(1)
        c = newc
    return c


def compute():
    c = binomial_coefficient(22)

    res = 0
    m = 75
    p = 1
    for n in range(22, -1, -1):
        if n % 2 == 0:
            res += c[n] * p
        else:
            res -= c[n] * p

        m += 1
        p *= m

    res *= 25 * 4 * 23
    p *= 99 * 100

    return res / p


if __name__ == "__main__":
    print(compute())
