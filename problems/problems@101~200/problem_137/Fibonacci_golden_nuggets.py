def generator():
    yield 1, 0
    # s^2 - 5 q^2 = 1
    # Basic solution to x^2 - 5 y^2 = 1 is (9, 4)
    x, y = 9, 4
    while True:
        yield x, y
        x, y = 9 * x + 20 * y, 9 * y + 4 * x


N = 4 * 10**9
res = []
for x, y in generator():
    # For even n, n = (s + q) q / 2
    # where s^2 - 5 q^2 = 4
    # Basic solutions are (3, 1), (18, 8)
    x0, y0 = 3, 1
    s = x0 * x + 5 * y0 * y
    q = x0 * y + y0 * x
    n = (s + q) * q // 2
    res.append(n)
    if n > N:
        break

for x, y in generator():
    x0, y0 = 18, 8
    s = x0 * x + 5 * y0 * y
    q = x0 * y + y0 * x
    n = (s + q) * q // 2
    res.append(n)
    if n > N:
        break

for x, y in generator():
    # for odd n, n = 4(s + 2 q) q - 1
    # where s^2 - 5 q^2 = -1
    # Basic solution is (2, 1)
    x0, y0 = 2, 1
    s = x0 * x + 5 * y0 * y
    q = x0 * y + y0 * x
    n = 4 * (s + 2 * q) * q - 1
    res.append(n)
    if n > N:
        break

print(sorted(res))
