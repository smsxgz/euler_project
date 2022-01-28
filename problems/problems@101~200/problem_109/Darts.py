def solve():
    res = 21  # only one throw to checkout

    double_darts = [50]
    darts = [25, 50]
    for i in range(1, 21):
        darts += [i, 2 * i, 3 * i]
        double_darts.append(2 * i)

    # two throw to checkout or first two throws are same
    for m in darts:
        for d in double_darts:
            if m + d < 100:
                res += 1
            if 2 * m + d < 100:
                res += 1

    n = 62
    for i in range(n-1):
        for j in range(i+1, n):
            for d in double_darts:
                if darts[i] + darts[j] + d < 100:
                    res += 1
    print(res)


if __name__ == '__main__':
    solve()
