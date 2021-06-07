from collections import defaultdict, Counter

cache = defaultdict(Counter)
for a in range(1, 10):
    cache[1][(a, a, a)] = 1

for i in range(2, 41):
    for a, b, c in cache[i - 1].keys():
        if c < 9:
            if c + 1 <= b:
                cache[i][(a, b, c + 1)] += cache[i - 1][(a, b, c)]
            else:
                cache[i][(a, c + 1, c + 1)] += cache[i - 1][(a, b, c)]

        if c > 0:
            if c - 1 >= a:
                cache[i][(a, b, c - 1)] += cache[i - 1][(a, b, c)]
            else:
                cache[i][(c - 1, b, c - 1)] += cache[i - 1][(a, b, c)]

res = 0
for i in range(10, 41):
    res += sum(cache[i][(0, 9, j)] for j in range(10))
print(res)
