import itertools


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


def all_not_empty_subset(lst):
    for i in range(1, len(lst) + 1):
        for subset in itertools.combinations(lst, i):
            yield subset


def to_number(digits, mask, c):
    res = 0
    for idx, k in enumerate(digits):
        if idx in mask:
            res = 10 * res + c
        else:
            res = 10 * res + k
    return res


def solve(primes):
    primes_set = set(primes)
    for p in primes:
        digits = [int(c) for c in str(p)]
        counter = {0: [], 1: [], 2: []}
        for idx, c in enumerate(digits):
            if c in counter:
                counter[c].append(idx)

        for c, slice in counter.items():
            for mask in all_not_empty_subset(slice):
                count = 1
                for j in range(c + 1, 10):
                    if to_number(digits, mask, j) in primes_set:
                        count += 1
                if count >= 8:
                    return p


if __name__ == '__main__':
    primes = euler_prime(10**6)
    import time

    start = time.time()
    print(solve(primes))
    print(time.time() - start)
