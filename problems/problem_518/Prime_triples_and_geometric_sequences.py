from mylib import euler_prime, gcd, sqrt

N = 10**8
# N = 100
primes = set(euler_prime(N))

res = 0
n = 0
for x in range(1, sqrt(N)):
    for k in range(1, N // (x * x) + 1):
        a = k * x * x - 1
        if a not in primes:
            continue

        for y in range(1, x):
            b = k * x * y - 1
            if b not in primes:
                continue
            c = k * y * y - 1
            if c not in primes:
                continue

            if gcd(x, y) > 1:
                continue

            res += a + b + c

print(res)
