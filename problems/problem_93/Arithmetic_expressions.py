from mylib import gcd

from itertools import permutations, product


class Number:
    def __init__(self, p, q=1):
        self.p = p
        self.q = q

    def add(self, other):
        return Number(self.p * other.q + self.q * other.p, self.q * other.q)

    def sub(self, other):
        return Number(self.p * other.q - self.q * other.p, self.q * other.q)

    def mul(self, other):
        return Number(self.p * other.p, self.q * other.q)

    def div(self, other):
        return Number(self.p * other.q, self.q * other.p)

    @property
    def _simple(self):
        d = gcd(abs(self.p), abs(self.q))
        self.p //= d
        self.q //= d
        return (self.p, self.q)

    def __repr__(self):
        return str((self.p, self.q))


def compute(nums, ops):
    a, b, c, d = nums
    res = []

    # (a b) (c d)
    res.append(
        a.__getattribute__(ops[0])(b).__getattribute__(ops[1])(
            c.__getattribute__(ops[2])(d))._simple)

    # ((a b) c) d
    res.append(
        a.__getattribute__(ops[0])(b).__getattribute__(
            ops[1])(c).__getattribute__(ops[2])(d)._simple)

    # (a (b c)) d
    res.append(
        a.__getattribute__(ops[0])(b.__getattribute__(
            ops[1])(c)).__getattribute__(ops[2])(d)._simple)

    # a ((b c) d)
    res.append(
        a.__getattribute__(ops[0])((b.__getattribute__(
            ops[1])(c)).__getattribute__(ops[2])(d))._simple)

    # a (b (c d))
    res.append(
        a.__getattribute__(ops[0])(b.__getattribute__(ops[1])(
            c.__getattribute__(ops[2])(d)))._simple)

    return res


def target_numbers(nums):
    nums = [Number(n) for n in nums]

    targets = set()
    for numsp in permutations(nums):
        for ops in product(['add', 'sub', 'mul', 'div'], repeat=3):
            for res in compute(numsp, ops):
                if res[1] == 1 and res[0] > 0:
                    targets.add(res[0])

    return sorted(list(targets))


def longest_consecutive(sorted_nums):
    i = 1
    while True:
        if sorted_nums[i - 1] != i:
            return i - 1
        i += 1


if __name__ == '__main__':
    N = 10
    longest = 28
    nums = [1, 2, 3, 4]

    for i in range(1, N - 3):
        for j in range(i + 1, N - 2):
            for k in range(j + 1, N - 1):
                for l in range(k + 1, N):
                    c = longest_consecutive(target_numbers([i, j, k, l]))
                    if c > longest:
                        longest = c
                        nums = [i, j, k, l]

    print(longest, nums)
