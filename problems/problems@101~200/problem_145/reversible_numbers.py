def solve(k):
    if k % 2 == 0:
        return 20 * (30**(k // 2 - 1))

    elif k % 4 == 1:
        return 0

    else:
        s = (k + 1) // 4
        return 5 * (20**s) * (25**(s - 1))


def main(k):
    print(sum(solve(kk) for kk in range(1, k + 1)))


if __name__ == '__main__':
    main(9)
