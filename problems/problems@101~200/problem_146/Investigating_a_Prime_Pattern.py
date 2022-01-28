from mylib import Miller_Rabin

res = 0
for n in range(1, 15000000):
    if n % 1000000 == 0:
        print(n, res)

    if n % 3 == 0:
        continue

    if n % 7 not in [1, 6]:
        continue

    s = n * n * 100
    for k in [1, 3, 7, 9, 11, 13, 17, 19, 21, 23, 27]:
        if k in [1, 3, 7, 9, 13, 27]:
            if not Miller_Rabin(s + k):
                break
        else:
            if Miller_Rabin(s + k):
                break
    else:
        res += 10 * n
print(res)
