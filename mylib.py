import time
import math


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


def sqrt1(n):
    left = 0
    right = n
    while left <= right:
        mid = (left + right) // 2
        if mid * mid > n:
            right = mid - 1
        elif (mid + 1) * (mid + 1) <= n:
            left = mid + 1
        else:
            return mid


def sqrt(n):
    return int(math.sqrt(n + 0.5))


def sqrt2(n):
    return int((n + 0.5)**(1 / 2))


def sqrt3(n):
    sq = n // 2
    while True:
        if sq * sq <= n and (sq + 1) * (sq + 1) > n:
            break
        sq = (sq + n // sq) // 2
    return sq


def power(n, k):
    assert n > 0
    m = power(n, k // 2)
    if k % 2 == 1:
        return m * m * n
    else:
        return m * m


def Eulid(n, m):
    while n > 0:
        n, m = m % n, n
    return m


gcd = Eulid


def extend_Eulid(n, m):
    """
        find k, l,
        s.t. k * n + l * m == gcd(n, m)
    """
    if not m:
        return 1, 0, n
    else:
        x, y, d = extend_Eulid(m, n % m)
        return y, x - y * (n // m), d


def inverse_mod(n, m):
    x, y, d = extend_Eulid(n, m)
    assert d == 1
    return x


def euler_func(n):
    phi = [0] * (n + 1)
    phi[1] = 1
    for i in range(2, n + 1):
        if not phi[i]:
            phi[i] = i - 1
            for j in range(i << 1, n + 1, i):
                if not phi[j]:
                    phi[j] = j
                phi[j] = phi[j] // i * (i - 1)
    return phi[1:]


if __name__ == '__main__':
    import numpy as np
    m, n = np.random.randint(5, 100, 2)
    print(m, n)
    x, y, d = extend_Eulid(m, n)
    print(x * m + y * n == d)
    euler_func(5)

    # %timeit sqrt(int(9e18))
    # %timeit sqrt1(int(9e18))
    # %timeit sqrt2(int(9e18))
    # %timeit sqrt3(int(9e18))
