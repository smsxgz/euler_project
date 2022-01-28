from mylib import euler_prime, power_mod


def helper(p):
    return power_mod(10, 10**9, p) == 1


def main():
    primes = euler_prime(200000)
    res = []
    for p in primes[2:]:
        if helper(p):
            res.append(p)
    print(res)
    print(len(res))
    print(sum(res[:40]))


if __name__ == "__main__":
    main()
