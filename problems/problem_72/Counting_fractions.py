from mylib import StopWatch, sqrt


def eulerPhi(n):
    phis = list(range(n + 1))
    for i in range(2, n + 1):
        if phis[i] == i:
            for j in range(i, n + 1, i):
                phis[j] = phis[j] - phis[j] // i
    return phis


def eulerPhi2(n):
    sieveLimit = sqrt(n)
    spf = [2 if i % 2 == 0 else i for i in range(n + 1)]
    for i in range(3, sieveLimit + 1, 2):
        if spf[i] == i:
            for m in range(i * i, n + 1, 2 * i):
                if spf[m] == m:
                    spf[m] = i

    phis = [0] * (n + 1)
    phis[1] = 1
    for i in range(2, n + 1):
        if spf[i] == i:
            phis[i] = i - 1
        else:
            p = spf[i]
            m = i // p
            factor = p if spf[m] == p else p - 1
            phis[i] = factor * phis[m]

    return phis


def solve(D):
    return sum(eulerPhi(D)) - 1


def solve2(D):
    return sum(eulerPhi2(D)) - 1


def solve3(D):
    sieveLimit = (sqrt(D) - 1) >> 1
    maxIndex = (D - 1) >> 1
    cache = [0] * (maxIndex + 1)
    for n in range(1, sieveLimit + 1):
        if cache[n] == 0:
            p = (n << 1) + 1
            for k in range(2 * n * (n + 1), maxIndex + 1, p):
                if cache[k] == 0:
                    cache[k] = p

    multiplier = 1
    while multiplier <= D:
        multiplier = multiplier << 1

    multiplier = multiplier >> 1
    fractionCount = multiplier - 1

    multiplier = multiplier >> 1
    stepIndex = (D // multiplier + 1) >> 1
    for n in range(1, maxIndex + 1):
        if n == stepIndex:
            multiplier = multiplier >> 1
            stepIndex = (D // multiplier + 1) >> 1

        if cache[n] == 0:
            cache[n] = n << 1
            fractionCount = fractionCount + multiplier * cache[n]
        else:
            p = cache[n]
            cofactor = ((n << 1) + 1) // p
            factor = p if cofactor % p == 0 else p - 1
            cache[n] = factor * cache[cofactor >> 1]
            fractionCount += multiplier * cache[n]

    return fractionCount


if __name__ == '__main__':
    with StopWatch():
        print(solve(1000000))

    with StopWatch():
        print(solve2(1000000))

    with StopWatch():
        print(solve3(1000000))
