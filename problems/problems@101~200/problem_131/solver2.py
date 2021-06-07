from mylib import euler_prime

primes = euler_prime(1000000)

res = 0
A = 1
a = 1
while A < 1000000:
    A += 6 * a
    a += 1

    if A in primes:
        res += 1

print(res)
