def generator():
    yield 1, 0
    # s^2 - 5 q^2 = 1
    # Basic solution to x^2 - 5 y^2 = 1 is (9, 4)
    x, y = 9, 4
    while True:
        yield x, y
        x, y = 9 * x + 20 * y, 9 * y + 4 * x


N = 4 * 10**10
res = []
for x, y in generator():
    for x0, y0 in [(7, 1), (8, 2), (13, 5), (17, 7), (32, 14), (43, 19)]:
        s = x0 * x + 5 * y0 * y
        q = x0 * y + y0 * x
        if (s - 7) % 5 == 0:
            # print(x0)
            res.append((s - 7) // 5)
    if len(res) > 40:
        break

res = sorted(res)
print(res)
print(sum(res[:31]))
