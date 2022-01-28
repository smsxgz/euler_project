from mylib import sqrt


def euler_sum(N):
    Imax = int((N + 0.5)**(1 / 3))
    D = N // Imax

    # compute S1
    prime = [1] * (D + 1)
    mobius = [1] * (D + 1)

    for i in range(2, D + 1):
        if not prime[i]:
            continue
        mobius[i] = -1
        for j in range(2, D // i + 1):
            prime[i * j] = 0
            mobius[i * j] *= -1
        for j in range(1, D // (i * i) + 1):
            mobius[j * i * i] = 0

    s1 = 0
    for i in range(1, D + 1):
        k = N // i
        s1 += mobius[i] * (k * (k + 1) // 2)

    # compute M(d), d = 1, ..., D
    M_list = [0]
    M = 0
    for m in mobius[1:]:
        M += m
        M_list.append(M)

    # compute M(n // i), i = Imax - 1, ..., 1
    Mxi_list = []
    Mxi_sum = 0
    for i in range(Imax - 1, 0, -1):
        Mxi = 1
        xi = N // i

        sqd = int(sqrt(xi))
        # we know that sqd < D <= xi
        for j in range(1, xi // (sqd + 1) + 1):
            Mxi -= (xi // j - xi // (j + 1)) * M_list[j]

        for j in range(2, sqd + 1):
            if xi // j <= D:
                Mxi -= M_list[xi // j]
            else:
                Mxi -= Mxi_list[Imax - j * i - 1]

        Mxi_list.append(Mxi)
        Mxi_sum += i * Mxi

    # compute S2
    s2 = Mxi_sum - Imax * (Imax - 1) // 2 * M_list[-1]
    return s1 + s2


def main(n):
    return ((n + 1) * n // 2 - euler_sum(n)) * 6


if __name__ == "__main__":
    print(main(5))
    print(main(10))
    print(main(1000))
    print(main(100000000))
