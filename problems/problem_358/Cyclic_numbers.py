from mylib import euler_prime, power_mod, sqrt

right = int(1 / 0.00000000137)
left = int(1 / 0.00000000138)
primes = euler_prime(sqrt(right))


def findPrimefactors(n):
    res = set()

    while n % 2 == 0:
        res.add(2)
        n = n // 2

    for p in primes:
        while (n % p == 0):
            res.add(p)
            n = n // p

    if n > 2:
        res.add(n)

    return list(res)


def is_primitive_root(n):
    for p in findPrimefactors(n - 1):
        if power_mod(10, (n - 1) // p, n) == 1:
            return False
    return True


def divide_digit_sum(n):
    m = 10
    digit_sum = 0
    for i in range(n - 1):
        digit_sum += m // n
        m = 10 * (m % n)
    return digit_sum


for n in range(left, right + 1):
    if (n * 56789) % 100000 == 99999:
        is_prime = True
        for p in primes:
            if n % p == 0:
                is_prime = False
                break
        if is_prime and is_primitive_root(n):
            print(n, divide_digit_sum(n))
