n = 0
for k in range(3, 17):
    m = 15 * 16**(k - 1) - (15**k + 2 * 14 * 15**
                            (k - 1)) + (2 * 14**k + 13 * 14**(k - 1)) - 13**k
    if k == 3:
        print(m)

    n += m

print(hex(n))
