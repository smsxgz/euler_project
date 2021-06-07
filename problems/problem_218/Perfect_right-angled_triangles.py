from mylib import gcd

N = 10000

res = 0
for s in range(2, N):
    for t in range(1, s):
        c = s**2 + t**2
        if c > 10**8:
            break

        if gcd(s, t) == 1:
            p = s**2 - t**2
            q = 2 * s * t
            S = abs(p**2 - q**2) * p * q
            if S % 84 != 0:
                res += 1
print(res)
