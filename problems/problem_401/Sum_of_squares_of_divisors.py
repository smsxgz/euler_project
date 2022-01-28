from mylib import sqrt


def solver(N):
    D = sqrt(N)

    # compute S1
    s1 = 0
    for d in range(1, D + 1):
        s1 += (N // d) * d * d

    # compute S2
    I = N // (D + 1)
    s2 = 0
    for i in range(1, I + 1):
        xi = N // i
        s2 += xi * (xi + 1) * (2 * xi + 1) // 6
    x = N // (I + 1)
    s2 -= I * (x + 1) * x * (2 * x + 1) // 6
    return s1 + s2


if __name__ == "__main__":
    print(solver(10**15))
