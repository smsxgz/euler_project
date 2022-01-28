from mylib import euler_prime, power_mod


def helper(p):
    # p > 3
    n = p - 1
    m = 1
    while n % 2 == 0:
        n //= 2
        m *= 2

    while n % 5 == 0:
        n //= 5
        m *= 5

    return power_mod(10, m, p) == 1


def main():
    primes = euler_prime(100000)
    res = 5
    for p in primes[2:]:
        if not helper(p):
            res += p
    print(res)


if __name__ == "__main__":
    main()
