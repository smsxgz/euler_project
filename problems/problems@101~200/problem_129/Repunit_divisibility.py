from mylib import euler_prime, sqrt, power_mod, Miller_Rabin

primes = euler_prime(2 * 10**3)


def primitivity_test(n):
    sq = sqrt(n)
    m = n - 1

    for p in primes:
        if p > sq:
            break

        if m % p == 0:
            if power_mod(10, (n - 1) // p, n) == 1:
                return False

            while m % p == 0:
                m //= p

    if m > 1:
        if power_mod(10, (n - 1) // m, n) == 1:
            return False

    return True


def helper(n):
    k = 0
    if n % 3 == 0:
        while n % 3 == 0:
            k += 1
            n //= 3

    if Miller_Rabin(n):
        if k == 0 and primitivity_test(n):
            return n - 1

        elif k > 0 and (n - 1) % 3 != 0 and primitivity_test(n):
            return 3**k * (n - 1)


def main():
    n = 10**6 + 1
    while True:
        r = helper(n)
        if r is not None and r > 10**6:
            print(n, r)
            break
        n += 1


if __name__ == "__main__":
    main()
