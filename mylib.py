import time


class StopWatch(object):
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
    k = 1
    while k * k <= n:
        k += 1
    return k - 1


def sqrt(n):
    k = 1
    while k * k <= n:
        k *= 2

    left = k // 2
    right = k
    while left + 1 < right:
        mid = (left + right) // 2
        if mid * mid <= n:
            left = mid
        else:
            right = mid
    return left


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
    pass
    import numpy as np
    m, n = np.random.randint(5, 100, 2)
    print(m, n)
    x, y, d = extend_Eulid(m, n)
    print(x * m + y * n == d)
    euler_func(5)
