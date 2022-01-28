from mylib import sqrt, gcd

mem = dict()
def divisor_sum(N):
    if N in mem:
        return mem[N]

    I = sqrt(N)

    s1 = 0
    for i in range(1, N // I + 1):
        s1 += i * (N // i)

    s2 = 0
    for i in range(1, I):
        xi = N // i
        s2 += (xi + 1) * xi // 2
    s2 -= (I - 1) * (N // I + 1) * (N // I) // 2

    r = s1 + s2
    mem[N] = r
    return r


def Gaussian_divisor_sum(N):
    sq = sqrt(N)

    res = divisor_sum(N)
    res += 2 * divisor_sum(N // 2)
    for a in range(2, sq + 1):
        for b in range(1, a):
            s = a * a + b * b
            if s > N:
                break
            if gcd(a, b) == 1:
                res += 2 * (a + b) * divisor_sum(N // s)

    print(res)


if __name__ == '__main__':
    from mylib import StopWatch
    with StopWatch():
        Gaussian_divisor_sum(10**8)
