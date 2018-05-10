import math
import time
import itertools


class StopWatch(object):
    def __enter__(self, *args):
        self.start = time.time()

    def __exit__(self, *args):
        print(time.time() - self.start)


'''
# Provides memoization for generating and testing pentagonal numbers.
class PentagonalNumberHelper(object):
    def __init__(self):
        self.term_list = [1]
        self.term_set = set([1])
        self.n = 1

    def term(self, x):
        assert x > 0
        while self.n <= x:
            term = (self.n * (self.n * 3 - 1)) >> 1
            self.n += 1
            self.term_list.append(term)
            self.term_set.add(term)
        return self.term_list[x]

    def is_term(self, y):
        assert y > 0
        while self.term_list[-1] < y:
            term = (self.n * (self.n * 3 - 1)) >> 1
            self.n += 1
            self.term_list.append(term)
            self.term_set.add(term)
        return y in self.term_set


def compute():
    pentanum = PentagonalNumberHelper()
    min_d = None
    for i in itertools.count(2):
        pent_i = pentanum.term(i)
        if min_d is not None and pent_i - pentanum.term(i - 1) >= min_d:
            break

        for j in range(i - 1, 0, -1):
            pent_j = pentanum.term(j)
            diff = pent_i - pent_j
            if min_d is not None and diff >= min_d:
                break
            elif pentanum.is_term(pent_i + pent_j) and pentanum.is_term(diff):
                min_d = diff
    return str(min_d)
'''


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


def is_pentagon(x):
    y = (math.sqrt(24 * x + 1) + 1) / 6
    return int(y) == y


def pentagon(n):
    return n * (3 * n - 1) >> 1


def main():
    for i in itertools.count(2):
        p_i = pentagon(i)
        for j in range(1, i):
            p_j = pentagon(j)
            if (p_i + p_j + j) % (3 * j) == 0:
                k = (p_i + p_j + j) // (3 * j)
                if is_pentagon(pentagon(k) + pentagon(k - j)):
                    print(k)
                    return p_i


# with StopWatch():
#     print(compute())

with StopWatch():
    print(main())
