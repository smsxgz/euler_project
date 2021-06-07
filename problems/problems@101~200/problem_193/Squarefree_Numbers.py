import time
from math import sqrt
import numba as nb


class StopWatch:
    def __enter__(self, *args):
        self.start = time.time()

    def __exit__(self, *args):
        print(time.time() - self.start)


def euler_prime(n):
    prime = []
    vis = [0] * (n + 1)
    for i in range(2, n + 1):
        if not vis[i]:
            prime.append(i)
        for p in prime:
            if i * p > n:
                break
            vis[i * p] = 1
            if (i % p == 0):
                break
    return prime


def Mobius(n):
    prime = [1] * (n + 1)
    mobius = [1] * (n + 1)

    for i in range(2, n + 1):
        if not prime[i]:
            continue
        mobius[i] = -1
        for j in range(2, n // i + 1):
            prime[i * j] = 0
            mobius[i * j] *= -1
        for j in range(1, n // (i * i) + 1):
            mobius[j * i * i] = 0
    return mobius


##########################################
@nb.njit
def square_free(n):
    sq = int(sqrt(n))

    prime = [1] * (sq + 1)
    mobius = [1] * (sq + 1)

    for i in range(2, sq + 1):
        if not prime[i]:
            continue
        mobius[i] = -1
        for j in range(2, sq // i + 1):
            prime[i * j] = 0
            mobius[i * j] *= -1
        for j in range(1, sq // (i * i) + 1):
            mobius[j * i * i] = 0

    s = 0
    for i in range(1, sq + 1):
        s += mobius[i] * (n // (i * i))
    return s


##########################################
# from fakesson
def euler193(L):
    pLst = euler_prime(int(sqrt(L)))
    pLst += [int(L**0.5) + 1]
    return euler193_helper(L, pLst)


@nb.njit
def euler193_helper(L, pLst):
    pLen = len(pLst)
    Q = [(1, L - 1, 0)]
    res = 0
    while len(Q) > 0:
        s, x, i = Q.pop()
        res += s * x
        flag = True
        for j in range(i, pLen):
            p = pLst[j]
            y = x // (p * p)
            if y == 0:
                break
            if flag:
                q = pLst[j + 1]
                if y < q * q:
                    flag = False
            if flag:
                Q += [(-s, y, j + 1)]
            else:
                res += -s * y
    return res


##########################################
@nb.njit
def efficient_square_free(N):
    Imax = int(N**(1 / 5))
    D = int(sqrt(N / Imax))

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
        s1 += mobius[i] * (N // (i * i))

    # compute M(d), d = 1, ..., D
    M_list = [0]
    M = 0
    for m in mobius[1:]:
        M += m
        M_list.append(M)

    # compute M(sqrt(n / i)), i = Imax - 1, ..., 1
    Mxi_list = []
    Mxi_sum = 0
    for i in range(Imax - 1, 0, -1):
        Mxi = 1
        xi = int(sqrt(N // i))

        sqd = int(sqrt(xi))
        # sqd < D <= xi
        for j in range(1, xi // (sqd + 1) + 1):
            Mxi -= (xi // j - xi // (j + 1)) * M_list[j]

        for j in range(2, sqd + 1):
            if xi // j <= D:
                Mxi -= M_list[xi // j]
            else:
                Mxi -= Mxi_list[Imax - j * j * i - 1]

        Mxi_list.append(Mxi)
        Mxi_sum += Mxi

    # compute S2
    s2 = Mxi_sum - (Imax - 1) * M_list[-1]
    return s1 + s2


if __name__ == '__main__':
    N = 2**52
    # N = 1000
    # with StopWatch():
    #     square_free(N)

    with StopWatch():
        efficient_square_free(N)

    # with StopWatch():
    #     print(euler193(N))
