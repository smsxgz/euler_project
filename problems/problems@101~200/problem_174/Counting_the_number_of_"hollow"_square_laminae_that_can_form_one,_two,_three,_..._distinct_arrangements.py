N = 10**6 // 4

factors = [1] * (N + 1)
for d in range(2, N + 1):
    for i in range(1, N // d + 1):
        factors[d * i] += 1

res = 0
for d in range(2, N + 1):
    if factors[d] <= 21:
        res += 1
print(factors[8])
print(res)
