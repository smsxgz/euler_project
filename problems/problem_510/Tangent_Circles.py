from mylib import gcd, sqrt

N = 10**9
# N = 100
sq = sqrt(sqrt(N))

res = 0
for y in range(1, sq + 1):
    for x in range(1, y + 1):
        if gcd(x, y) > 1:
            continue
        n = (x + y)**2
        # for k in range(1, N // (y**2 * n)):
        #     r = k * x**2 * y**2
        #     res += k * (x**2 + y**2) * n + k * x**2 * y**2
        k = N // (y**2 * n)
        res += k * (k + 1) // 2 * ((x**2 + y**2) * n + x**2 * y**2)
print(res)
