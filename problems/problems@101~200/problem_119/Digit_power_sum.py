from math import log10

res = []

for d in range(2, 20):
    n = 2
    while n <= 9 * (d * log10(n) + 1):
        N = n**d
        if sum(int(ch) for ch in str(N)) == n:
            res.append([n, d, N])
        n += 1

res = sorted(res, key=lambda x: x[-1])
print(res[29])
