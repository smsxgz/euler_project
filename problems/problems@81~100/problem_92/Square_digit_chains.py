import time


def digit_square(n):
    s = 0
    while n > 0:
        k = n % 10
        s += k**2
        n = n // 10
    return s


def Square_digit_chains(n):
    try:
        k = d[n]
    except KeyError:
        m = digit_square(n)
        k = Square_digit_chains(m)
        d[m] = k
    d[n] = k
    return k


N = 7 * 81
start = time.time()
d = {1: 1, 89: 89}
count = 0
for i in range(2, N):
    if Square_digit_chains(i) == 89:
        count += 1

for i in range(2, N):
    j = digit_square(i)
    if d[j] == 89:
        count += 1

print(time.time() - start)
print(count)
