N = 50000000

cache = dict()
for n in range(2, N):
    for k in range(4 - (n % 4), min(3 * n - 3, N // n + 1), 4):
        m = n * k
        if m in cache:
            cache[m] += 1
        else:
            cache[m] = 1

res = 0
for key in cache:
    if cache[key] == 1 and key < N:
        res += 1
print(res)
