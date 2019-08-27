def solve(n=100):
    patition = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    patition[1][1] = 1
    for i in range(2, n + 1):
        for j in range(1, i + 1):
            patition[i][j] = patition[i - j][j] + patition[i - 1][j - 1]
    return sum(patition[-1][2:])


def solve2(n=100):
    patition = [1] + [0] * n
    for i in range(1, n):
        for j in range(i, n + 1):
            patition[j] = patition[j] + patition[j - i]
    return patition[-1]


if __name__ == '__main__':
    solve2(100)
