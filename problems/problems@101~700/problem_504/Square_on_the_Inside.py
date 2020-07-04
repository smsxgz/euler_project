from mylib import StopWatch


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def solve(N=100):
    table = []
    for i in range(1, N + 1):
        tmp = []
        for j in range(1, N + 1):
            tmp.append(i * j - gcd(i, j))
        table.append(tmp)

    squares = set()
    i = 1
    k = 1
    while k < 2 * N * N:
        squares.add(k)
        k += 2 * i + 1
        i += 1

    res = 0
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            for c in range(1, N + 1):
                for d in range(1, N + 1):
                    points = (
                        table[a - 1][b - 1] + table[b - 1][c - 1] +
                        table[c - 1][d - 1] + table[d - 1][a - 1]) // 2 + 1
                    res += (points in squares)
    return res


def solve2(N=100):
    table = []
    for i in range(1, N + 1):
        tmp = []
        for j in range(1, N + 1):
            tmp.append(i * j - gcd(i, j))
        table.append(tmp)

    squares = set()
    i = 1
    k = 1
    while k < 2 * N * N:
        squares.add(2 * k)
        k += 2 * i + 1
        i += 1

    res = 0
    for a in range(1, N + 1):
        for c in range(1, N + 1):
            vb = set()
            for b in range(1, N + 1):
                vb.add(table[a - 1][b - 1] + table[c - 1][b - 1] + 1)
            upper = 2 * max(vb)
            for v in vb:
                for s in squares:
                    if s > upper:
                        break
                    res += (s - v) in vb


if __name__ == "__main__":
    # with StopWatch():
    #     print(solve())

    with StopWatch():
        print(solve2())
