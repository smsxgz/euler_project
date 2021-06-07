from math import log10, sqrt


def first_digits(k):
    s = k * log10((sqrt(5) + 1) / 2) - log10(5) / 2
    s -= int(s) - 8
    return int(10**s)


mod = 10**9
count = 2
F1 = 1
F2 = 1
while True:
    F1, F2 = F2, (F1 + F2) % mod
    count += 1
    # if set(str(F2)) == set('123456789'):
    if set(str(F2)) == set('123456789') and set(str(
            first_digits(count))) == set('123456789'):
        print(count)
        break
