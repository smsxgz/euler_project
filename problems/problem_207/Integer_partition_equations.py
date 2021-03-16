p4 = 4
p2 = 2
perfect = 0
k = 1
while True:
    m = k * (k + 1)
    if p4 - p2 == m:
        p4 *= 4
        p2 *= 2
        perfect += 1

    if perfect * 12345 < k:
        break

    if m in [12, 20, 30]:
        print(perfect / k)

    k += 1

print(k, k * (k + 1))
