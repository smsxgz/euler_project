from mylib import gcd, sqrt


def is_square(n):
    s = sqrt(n)
    return s * s == n


N = 10**12
sq = 10**4
# N = 100000
# sq = int((N + 0.5)**(1 / 3))

res = 0
for y in range(1, sq):
    y3 = y**3
    for k in range(1, sqrt(N // y3) + 1):
        for x in range(1, y):
            if gcd(x, y) > 1:
                continue

            m = k * x * (k * y3 + x)
            if m > N:
                break

            if is_square(m):
                # print(m, sqrt(m), k, x, y)
                res += m
print(res)
