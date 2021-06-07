from mylib import sqrt


def euler_func(n):
    sieveLimit = sqrt(n)
    spf = [2 if i % 2 == 0 else i for i in range(n + 1)]
    for i in range(3, sieveLimit + 1, 2):
        if spf[i] == i:
            for m in range(i * i, n + 1, 2 * i):
                if spf[m] == m:
                    spf[m] = i

    phis = [0] * (n + 1)
    chains = [1] * (n + 1)
    phis[1] = 1
    res = 0
    for i in range(2, n + 1):
        if spf[i] == i:
            phis[i] = i - 1
        else:
            p = spf[i]
            m = i // p
            factor = p if spf[m] == p else p - 1
            phis[i] = factor * phis[m]

        chains[i] = 1 + chains[phis[i]]
        if spf[i] == i and chains[i] == 25:
            res += i

    return res


if __name__ == "__main__":
    from mylib import StopWatch

    with StopWatch():
        print(euler_func(40000000))
