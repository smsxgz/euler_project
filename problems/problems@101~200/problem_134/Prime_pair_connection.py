from mylib import inverse_mod, euler_prime

primes = euler_prime(1100000)[2:]


def solve(p1, p2):
    mod = 10
    while p1 > mod:
        mod *= 10

    n = (inverse_mod(p2, mod) * p1) % mod
    return n * p2


def compute():
    res = 0
    for i in range(len(primes)):
        p1 = primes[i]
        p2 = primes[i + 1]
        if p1 > 1000000:
            break

        res += solve(p1, p2)
    print(res)


if __name__ == "__main__":
    compute()
