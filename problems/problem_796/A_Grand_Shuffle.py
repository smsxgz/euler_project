from fractions import Fraction


def helper():
    c = 1
    s = 1
    res = 0
    for i in range(13):
        m = 4 * i + 2
        res += s * c * Fraction(55, 55 - m)

        c = c * (13 - i) // (i + 1)
        s *= -1
    return res


cache = dict()
for n in [4, 10, 13]:
    cache[(n, 0)] = 1
    for i in range(n):
        cache[(n, i + 1)] = cache[(n, i)] * (n - i) // (i + 1)


def solve():
    N = 540
    res = 0
    for x in range(5):
        for y in range(11):
            for z in range(14):
                m = y * (x * z + 2)
                c = cache[(4, x)] * cache[(10, y)] * cache[(13, z)]
                if (x + y + z) % 2 == 1:
                    s = 1
                else:
                    s = -1

                res += s * c * Fraction(N + 1, N + 1 - m)
    return N + 1 - res


if __name__ == "__main__":
    r = solve()
    print(r)
    print(float(r))
