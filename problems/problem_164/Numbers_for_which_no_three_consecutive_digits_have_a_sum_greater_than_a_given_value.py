from collections import defaultdict, Counter

# n digits number which end with (a, b) where a + b <= 9
res = defaultdict(Counter)
for a in range(1, 10):
    for b in range(10 - a):
        res[2][(a, b)] = 1

for n in range(3, 21):
    for a in range(10):
        for b in range(10 - a):
            for c in range(10 - a - b):
                res[n][(a, b)] += res[n - 1][(c, a)]

print(sum(res[20].values()))
