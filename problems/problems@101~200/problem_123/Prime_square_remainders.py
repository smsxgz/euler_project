from mylib import euler_prime

prime = euler_prime(10**6)

N = 10**10
for idx, p in enumerate(prime):
    if idx % 2 == 0 and 2 * (idx + 1) * p > N:
        print(idx + 1)
        break
