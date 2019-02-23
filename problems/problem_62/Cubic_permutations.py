def solve(k=5):
    counter = dict()

    x = 1
    y = 1
    while True:
        c = [0 for _ in range(10)]
        t = y
        while t > 0:
            t, r = divmod(t, 10)
            c[r] += 1
        c = tuple(c)
        if c not in counter:
            counter[c] = {'number': 0, 'root': []}
        counter[c]['number'] += 1
        counter[c]['root'].append(x)

        if counter[c]['number'] == k:
            print(c, counter[c]['root'])
            return counter[c]['root']

        y += 3 * x * (x + 1) + 1
        x += 1


if __name__ == '__main__':
    solve(5)
