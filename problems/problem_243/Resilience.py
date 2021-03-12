from mylib import euler_prime

primes = euler_prime(100)

r = 15499 / 94744
idx = 0
n = 1
while r < 1:
    p = primes[idx]
    r *= p / (p - 1)
    n *= p
    print(p)
    idx += 1

N = int(1 / (r - 1) + 1)

print(N, n, 4 * n)
