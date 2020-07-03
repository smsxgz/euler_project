from math import sqrt, log10, ceil

res = 0
for p in range(1, 1006):
    for q in range(p + 1, 2012 - p):
        s = -log10(sqrt(q) - sqrt(p))
        if s > 0:
            r = ceil(2011 / s)
            res += (r + 1) // 2

print(res)
