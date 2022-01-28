from mylib import euler_prime, sqrt

N = 999966663333
sq = sqrt(N)
primes = euler_prime(2 * sq)
# n = len(primes)

i = 0
res = 0
while True:
    p = primes[i]
    q = primes[i + 1]

    if p * p > N:
        break

    # left divisible
    upper = min(q * q // p, N // p)
    lower = p + 1
    res += p * ((upper - lower + 1) * (lower + upper) // 2 - q * (upper >= q))

    # right divisible
    upper = min(q - 1, N // q)
    lower = p * p // q + 1
    res += q * ((upper - lower + 1) * (lower + upper) // 2 - p * (upper >= p))

    i += 1

print(res)
