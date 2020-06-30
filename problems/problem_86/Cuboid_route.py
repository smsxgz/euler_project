from mylib import gcd, sqrt

M = 2000
sq = (sqrt(4 * M + 1) + 1) // 2

cache = []
for p in range(1, sq):
    for q in range(p + 1, M // p + 1, 2):
        if gcd(p, q) == 1:
            a = 2 * p * q
            b = q**2 - p**2
            if min(a, b) > M:
                break
            cache.append((a, b))


def solve(m):
    res = 0
    for a, b in cache:
        if m % b == 0:
            aa = m // b * a
            res += min(max(0, (2 * m + 2 - aa) // 2), aa // 2)
        if m % a == 0:
            bb = m // a * b
            res += min(max(0, (2 * m + 2 - bb) // 2), bb // 2)
    return res


def main(N):
    res = 0
    m = 3
    while True:
        res += solve(m)
        if res > N:
            print(m)
            break
        m += 1


if __name__ == '__main__':
    main(10**6)
