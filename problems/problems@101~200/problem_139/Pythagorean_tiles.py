from mylib import gcd, sqrt

N = 10**8
sq = sqrt(N // 2)

res = 0
for p in range(2, sq + 1):
    for q in range(p % 2 + 1, p, 2):
        if 2 * p * (p + q) >= N:
            break

        if gcd(p, q) > 1:
            continue

        a = p**2 - q**2
        b = 2 * p * q
        c = p**2 + q**2

        if c % abs(a - b) == 0:
            res += (N - 1) // (2 * p * (p + q))

print(res)
