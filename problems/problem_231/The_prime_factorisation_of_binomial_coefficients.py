from mylib import euler_prime

primes = euler_prime(2 * 10**7)


def count(n, p):
    res = 0
    while n > 0:
        n //= p
        res += n
    return res


def solve(n, k):
    res = 0
    for p in primes:
        m = count(n, p) - count(k, p) - count(n - k, p)
        res += m * p
    print(res)


if __name__ == '__main__':
    solve(2 * 10**7, 5 * 10**6)
