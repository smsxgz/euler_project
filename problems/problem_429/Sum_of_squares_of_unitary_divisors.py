from mylib import euler_prime, power_mod

mod = 1000000009
N = 10**8
primes = euler_prime(N)

res = 1
for p in primes:
    q = p
    m = 0
    while q < N:
        m += N // q
        q *= p
    res *= 1 + power_mod(p, 2 * m, mod)
    res %= mod
print(res)
