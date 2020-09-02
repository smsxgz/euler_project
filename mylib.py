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
    if k == 0:
        return 1

    if k == 1:
        return n

    m = power(n, k // 2)
    if k % 2 == 1:
        return m * m * n
    else:
        return m * m


def power_mod(n, k, M):
    if k == 0:
        return 1

    if k == 1:
        return n

    m = power_mod(n, k // 2, M)
    if k % 2 == 1:
        return (m * m * n) % M
    else:
        return (m * m) % M


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


def Miller_Rabin(n):
    test = [2, 3, 5, 7, 11, 13, 17]
    if n in test:
        return True

    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1

    for a in test:
        x = power_mod(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True


def combinations(lst, k, prefix=[]):
    if len(lst) == k:
        yield prefix + lst
        return

    if k == 0:
        yield prefix
        return

    yield from combinations(lst[1:], k - 1, prefix + [lst[0]])
    yield from combinations(lst[1:], k, prefix)


if __name__ == '__main__':
    print(Miller_Rabin(211))
