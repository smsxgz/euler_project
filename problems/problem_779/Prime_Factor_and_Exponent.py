from mylib import euler_prime

primes = euler_prime(1000000)
res = 0
for p in primes[::-1]:
    res = res * (p - 1) / p + 1 / (p * (p - 1) * (p - 1))
print(res)
