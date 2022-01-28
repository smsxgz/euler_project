from mylib import euler_prime, Miller_Rabin
from bisect import bisect_right


def admissible_numbers(N, primes, m=1):
    if len(primes) == 0:
        return

    p = primes[0]
    n = p
    while n <= N // m:
        yield n * m
        yield from admissible_numbers(N, primes[1:], n * m)
        n *= p


def main():
    N = 10 ** 9
    nums = list(admissible_numbers(N, [2, 3, 5, 7, 11, 13, 17, 19, 23]))
    nums.sort()

    primes = euler_prime(10 ** 6)

    res = set()

    idx = bisect_right(nums, 10 ** 6)
    for n in nums[:idx]:
        i = bisect_right(primes, n + 1)
        res.add(primes[i] - n)

    for n in nums[idx:]:
        m = 3
        while True:
            if Miller_Rabin(n + m):
                res.add(m)
                break
            m += 2
    print(sum(res))


if __name__ == "__main__":
    main()
