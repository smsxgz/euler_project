def solve(matrix, size):
    x, y = size

    for j in range(1, y):
        matrix[(0, j)] += matrix[(0, j - 1)]
    for i in range(1, x):
        matrix[(i, 0)] += matrix[(i - 1, 0)]
    for i in range(1, x):
        for j in range(1, y):
            matrix[(i, j)] += min(matrix[(i - 1, j)], matrix[(i, j - 1)])

    return matrix[(x - 1, y - 1)]


def main():
    matrix = {}
    with open('matrix.txt', 'r') as f:
        for i, line in enumerate(f.readlines()):
            for j, s in enumerate(line.strip().split(',')):
                matrix[(i, j)] = int(s)
    r, c = sorted(matrix.keys(), key=lambda x: sum(x))[-1]
    print(solve(matrix, (r + 1, c + 1)))


if __name__ == '__main__':
    main()
