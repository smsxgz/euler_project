from collections import Counter

N = 10**6

counter = Counter()
m = 1
while True:
    k0 = m // 3 + 1
    if k0 + m >= N:
        break

    k = k0
    while True:
        n = (k + m) * (3 * k - m)
        if n >= N:
            break
        counter[n] += 1
        k += 1

    m += 1

res = 0
for key in counter:
    if counter[key] == 10:
        # print(key)
        res += 1
print(res)
