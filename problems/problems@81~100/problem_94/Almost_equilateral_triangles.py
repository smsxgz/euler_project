import math
import time
import itertools

# stupid method 1
start = time.time()
N = ((10**9 - 1) // 3 - 1) // 2 + 1
N
sum_perimeters = 0
s = 1
j = 1
for i in range(1, N):
    n = i * (3 * i + 2)
    while n >= s:
        if n == s:
            sum_perimeters += 6 * i + 4
            break
        s += 2 * j + 1
        j += 1

    n = (i + 1) * (3 * i + 1)
    while n >= s:
        if n == s:
            sum_perimeters += 6 * i + 2
            break
        s += 2 * j + 1
        j += 1

print(sum_perimeters)
print(time.time() - start)


# stupid methed 2
def compute():
    LIMIT = 10**9
    ans = 0
    for s in itertools.count(1, 2):
        if s * s > (LIMIT + 1) // 3:
            break
        for t in range(s - 2, 0, -2):
            if math.gcd(s, t) == 1:
                a = s * t
                b = (s * s - t * t) // 2
                c = (s * s + t * t) // 2
                if a * 2 == c - 1:
                    p = c * 3 - 1
                    if p <= LIMIT:
                        ans += p
                if a * 2 == c + 1:
                    p = c * 3 + 1
                    if p <= LIMIT:
                        ans += p
                if b * 2 == c - 1:
                    p = c * 3 - 1
                    if p <= LIMIT:
                        ans += p
                if b * 2 == c + 1:
                    p = c * 3 + 1
                    if p <= LIMIT:
                        ans += p
    return str(ans)


start = time.time()
print(compute())
print(time.time() - start)
