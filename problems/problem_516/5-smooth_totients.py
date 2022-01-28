import numpy as np
from bisect import bisect_left
from mylib import Miller_Rabin


def Hamming_number_generator(n):
    res = []
    a = int(np.log(n) / np.log(5))
    for i in range(a + 1):
        b = int((np.log(n) - i * np.log(5)) / np.log(3))
        for j in range(b + 1):
            c = int((np.log(n) - i * np.log(5) - j * np.log(3)) / np.log(2))
            for k in range(c + 1):
                res.append(2**k * 3**j * 5**i)
    res.sort()
    return res


# def helper(n, nums):
#     if len(nums) == 0:
#         return Hamming_number_count(n)

#     p = nums[0]
#     return helper(n, nums[1:]) + p * helper(n // p, nums[1:])


def main(n):
    Hamming_nums = Hamming_number_generator(n)
    Hamming_sums = [0]
    s = 0
    for i in range(len(Hamming_nums)):
        s += Hamming_nums[i]
        Hamming_sums.append(s)

    primes = []
    for m in Hamming_nums:
        if Miller_Rabin(m + 1):
            primes.append(m + 1)
    primes = primes[3:]

    # print(primes)

    def helper(n, nums):
        if len(nums) == 0:
            i = bisect_left(Hamming_nums, n)
            if Hamming_nums[i] == n:
                i += 1
            return Hamming_sums[i]

        p = nums[0]
        if n >= p:
            return helper(n, nums[1:]) + p * helper(n // p, nums[1:])
        else:
            return helper(n, [])

    print(helper(n, primes) % 2**32)


if __name__ == "__main__":
    main(100)
    main(10**12)
