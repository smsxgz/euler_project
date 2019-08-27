from math import log10, floor

res = 3
for i in range(4, 10):
    res += floor(1 / log10(10 / i))
print(res)
