import numpy as np
from mylib import euler_prime
from bisect import bisect_left

digits = np.array([[1, 1, 1, 0, 1, 1, 1],
                   [0, 0, 1, 0, 0, 1, 0],
                   [1, 0, 1, 1, 1, 0, 1],
                   [1, 0, 1, 1, 0, 1, 1],
                   [0, 1, 1, 1, 0, 1, 0],
                   [1, 1, 0, 1, 0, 1, 1],
                   [1, 1, 0, 1, 1, 1, 1],
                   [1, 1, 1, 0, 0, 1, 0],
                   [1, 1, 1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 0, 1, 1]], dtype='int8')

segments = dict()
dist = dict()
for i in range(10):
    segments[i] = sum(digits[i])
    for j in range(10):
        dist[(i, j)] = sum(abs(digits[i] - digits[j]))


def helper(n):
    nums = []
    while n > 0:
        n, r = divmod(n, 10)
        nums.append(r)
    return nums


def sam_clock(n):
    res = 0
    while n >= 10:
        nums = helper(n)
        for d in nums:
            res += 2 * segments[d]
        n = sum(nums)
    return res + 2 * segments[n]


def max_clock(n):
    res = 0
    nums = helper(n)
    for d in nums:
        res += segments[d]

    while True:
        tn = sum(nums)
        tnums = helper(tn)

        for i in range(len(nums)):
            if i < len(tnums):
                res += dist[(nums[i], tnums[i])]
            else:
                res += segments[nums[i]]

        n = tn
        nums = tnums

        if tn < 10:
            res += segments[tn]
            break
    return res


if __name__ == '__main__':
    print(sam_clock(137))
    print(max_clock(137))

    primes = euler_prime(2 * 10**7)
    idx = bisect_left(primes, 10**7)
    primes = primes[idx:]

    res = 0
    for p in primes:
        res += sam_clock(p) - max_clock(p)
    print(res)
