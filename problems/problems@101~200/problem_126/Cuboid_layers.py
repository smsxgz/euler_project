from collections import Counter
from mylib import sqrt

A = 100
N = 3 * A * A + 1

counter = Counter()
for a in range(1, A + 1):
    B = sqrt(a * a + N) - a
    for b in range(a, B + 1):
        for c in range(b, (N - a * b) // (a + b) + 1):
            k = 0
            n = a * b + c * (a + b)
            counter[n] += 1
            while n < N:
                n += 2 * (a + b + c) + 4 * k
                k += 1
                counter[n] += 1

res = []
for n in counter:
    if counter[n] == 10:
        res.append(n)
print(2 * min(res))

res = []
for n in counter:
    if counter[n] == 1000:
        res.append(n)
print(2 * min(res))
