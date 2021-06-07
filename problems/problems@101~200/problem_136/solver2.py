# k = (n+x^2)/(4x) (k < x) must be unique
# n must satisfies
# (1) n = 4p with p odd prime or p=1.
# (2) n = 16p with p odd prime or p=1.
# (3) n = p with p prime and p+1 mod 4 = 0.

from mylib import euler_prime

N = 50000000
primes = euler_prime(N)

res = 2
for p in primes:
    if p % 4 == 3:
        res += 1
    if 4 * p < N:
        res += 1
    if 16 * p < N:
        res += 1
print(res)
