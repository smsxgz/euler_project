# author: inamori

from itertools import takewhile, chain
from functools import reduce
from math import sqrt
from queue import PriorityQueue
import time


class cPrimes:
    def __init__(self, N):
        self.L = N // 96 + 1
        self.N = self.L * 96
        self.sieve()

    def sieve(self):
        self.bits = [-1] * self.L
        self.bits[0] &= ~1
        for p in takewhile(lambda p: p * p < self.N, self.enumerate2()):
            k0 = p // 3
            for k in range(k0 + p * 2, self.N // 3, p * 2):
                self.erase_bit(k)
            for k in range(-k0 - 1 + p * 2, self.N // 3, p * 2):
                self.erase_bit(k)

    def enumerate(self):
        return chain((2, 3), self.enumerate2())

    # maximal p < n
    def max_prime(self, n):
        if n <= 5:
            if n == 5:
                return 3
            elif n >= 3:
                return n - 1
            else:
                return 0
        else:
            if n % 6 <= 1:
                k0 = n // 3 - 1
            else:
                k0 = n // 6 * 2
            self.expand(k0 >> 5)
            for k in range(k0, -1, -1):
                m = k >> 5
                l = k & 31
                if ((self.bits[m] >> l) & 1) == 1:
                    return m * 96 + l * 3 + 1 + (l & 1)

    def enumerate2(self):
        for m, B in enumerate(self.bits):
            for k in range(32):
                if ((B >> k) & 1) == 1:
                    yield m * 96 + k * 3 + 1 + (k & 1)

    def erase_bit(self, k):
        m = k >> 5
        l = k & 31
        if l != 31:
            self.bits[m] &= ~(1 << l)
        else:
            self.bits[m] &= ~(-1 << 31)

    def expand(self, n):
        while n >= self.L:
            self.N *= 2
            self.L *= 2
            self.sieve()


def value_f(fs):
    # return reduce(lambda x, (p, e): x * p**e, fs, 1)
    return reduce(lambda x, y: x * y[0]**y[1], fs, 1)


def phi(fs):
    return reduce(lambda x, y: x * y[0]**(y[1] - 1) * (y[0] - 1), fs, 1)


def phi_ratio(fs):
    a = reduce(lambda x, y: x * y[0], fs, 1)
    b = reduce(lambda x, y: x * (y[0] - 1), fs, 1)
    return MyFrac(a, b)


class MyFrac:
    def __init__(self, a, b):
        self.a, self.b = a, b

    def __lt__(self, f):
        return self.a * f.b < self.b * f.a


def nexts(fs0):
    p, e = fs0[-1]

    # ((5, 2),) -> ((5, 3),)
    if value_f(fs0) * p < N:
        yield fs0[:-1] + ((p, e + 1), )

    # ((5, 2),) -> ((5, 1), (19, 1))
    if e >= 2:
        p_max = primes.max_prime((N - 1) // value_f(fs0[:-1] +
                                                    ((p, e - 1), )) + 1)
        if p_max > p:
            yield fs0[:-1] + ((p, e - 1), (p_max, 1))

    # ((5, 1), (19, 1)) -> ((5, 1), (17, 1))
    else:
        p_max = primes.max_prime(p)
        if p_max > fs0[-2][0]:
            yield fs0[:-1] + ((p_max, 1), )

    # ((5, 2),) -> ((3, 2),)
    if len(fs0) == 1 and e == 2 and p >= 3:
        p_max = primes.max_prime(p)
        yield ((p_max, e), )


def numbers_sorted_by_phi_ratio(N):
    pq = PriorityQueue()
    fs0 = ((primes.max_prime(int(sqrt(N)) + 1), 2), )
    pq.put((phi_ratio(fs0), fs0))
    while not pq.empty():
        r, fs = pq.get()
        yield fs
        for next_fs in nexts(fs):
            pq.put((phi_ratio(next_fs), next_fs))


def digits(n):
    while n != 0:
        yield n % 10
        n //= 10


def is_permutation(m, n):
    return sorted(list(digits(m))) == sorted(list(digits(n)))


t0 = time.time()
N = 10**7
primes = cPrimes(int(sqrt(N)) * 2)
print(
    next(
        value_f(fs) for fs in numbers_sorted_by_phi_ratio(N)
        if is_permutation(value_f(fs), phi(fs))))
print(time.time() - t0)
