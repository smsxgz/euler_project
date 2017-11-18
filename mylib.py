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


if __name__ == '__main__':
    import random
    with StopWatch():
        for _ in range(1000):
            sqrt(1234567890)
    with StopWatch():
        for _ in range(1000):
            sqrt1(1234567890)

    print(sqrt(1234567890), sqrt1(1234567890))
