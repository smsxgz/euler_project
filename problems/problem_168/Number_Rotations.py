def lst2num(lst):
    n = 0
    for m in lst:
        n = 10 * n + m
    return n


def solve(d, k):
    k0 = k
    path = [k]
    i = 0
    while True:
        i, k = divmod(d * k + i, 10)
        if k == k0 and i == 0:
            return path
        path.append(k)

        if len(path) > 100:
            return []


def solve2(d, k, m):
    k0 = k
    path = [k]
    i = 0
    for _ in range(m):
        i, k = divmod(d * k + i, 10)
        path.append(k)

    if k == k0 and i == 0:
        return path[:-1]


def main(N):
    res = 0
    for d in range(2, 10):
        for k in range(1, 10):
            path = solve(d, k)
            if path and path[-1] != 0:
                # leading zeros are disallowed
                res += lst2num(path[:5][::-1]) * (N // len(path))
                res %= 100000
    res += (1233 + 11111 * (N - 4)) * 45
    res %= 100000

    return res


if __name__ == "__main__":
    # print(solve2(5, 7, 8))
    print(main(100))
