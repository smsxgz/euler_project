def is_square(n):
    queue = []
    while n > 0:
        queue.append(n % 100)
        n //= 100

    res = []
    a = 0
    r = 0
    while queue:
        r *= 100
        r += queue.pop(-1)
        a *= 10
        for i in range(10):
            u = 2 * a + 2 * i + 1
            if r >= u:
                r -= u
            else:
                res.append(i)
                break
        a += res[-1]

    if r == 0:
        sq = 0
        for m in res:
            sq = sq * 10 + m
        return sq


def solve():
    a, b, c, d = 2, 7, 3, 5
    odd = 1
    while True:
        if odd:
            yield b * c, c * d
        else:
            yield 2 * b * c, c * d
        odd = 1 - odd

        a, b, c, d = b, a + 2 * d, d, c + 2 * b


N = 10**12
for item in solve():
    if item[0] > N:
        print(item)
        break
