import itertools


def solve(matrix):
    n = len(matrix)
    cache = dict()

    for i in range(n):
        cache[(i, )] = matrix[-1][i]

    for i in range(2, n + 1):
        tmp_cache = dict()
        for p in itertools.combinations(range(n), i):
            tmp = -1
            for idx in range(i):
                tmp = max(
                    tmp, matrix[-i][p[idx]] + cache[tuple(
                        [*p[:idx], *p[idx + 1:]])])
            tmp_cache[p] = tmp
        cache = tmp_cache
    return list(cache.values())[-1]


def memoize(f):
    memo = {}

    def helper(*args):
        if args not in memo:
            memo[args] = f(*args)
        return memo[args]

    return helper


def DPsolver(matrix):
    @memoize
    def f(A, B):
        """Maximum using rows A and columns B"""
        if len(A) == 0:
            return 0
        return max(matrix[A[0]][b] + f(A[1:], B[:j] + B[j + 1:])
                   for j, b in enumerate(B))

    return f(tuple(range(len(matrix))), tuple(range(len(matrix))))


def mprint(matrix):
    for line in matrix:
        print(', '.join(['{:4}'.format(j) for j in line]))
    print("+" * 30)
    print()


# https://en.wikipedia.org/wiki/Hungarian_algorithm
def Munkres_slove(matrix):
    n = len(matrix)

    def dfs(v):
        line = matrix[v]
        for u in range(n, 2 * n):
            if line[u - n] == 0 and check[u] == 0:
                check[u] = 1
                if matching[u] == -1 or dfs(matching[u]):
                    matching[u] = v
                    matching[v] = u
                    return True
        return False

    while True:
        for i in range(n):
            min_row = min(matrix[i][j] for j in range(n))
            for j in range(n):
                matrix[i][j] -= min_row

        for j in range(n):
            min_col = min(matrix[i][j] for i in range(n))
            for i in range(n):
                matrix[i][j] -= min_col
        # mprint(matrix)

        match = 0
        matching = dict((i, -1) for i in range(2 * n))
        for v in range(n):
            if matching[v] == -1:
                check = dict((j, 0) for j in range(2 * n))
                if dfs(v):
                    match += 1

        if match == n:
            return matching
        elif match > n:
            raise Exception('Something Wrong!')

        mark_row = []
        mark_col = []
        Q = [i for i in range(n) if matching[i] == -1]
        while Q:
            i = Q.pop(0)
            if i not in mark_row:
                mark_row.append(i)
                for j in range(n):
                    if matrix[i][j] == 0 and j not in mark_col:
                        mark_col.append(j)
                        Q.append(matching[j + n])

        remain_min = min(
            min(matrix[i][j] for j in range(n) if j not in mark_col)
            for i in mark_row)
        if remain_min == 0:
            break
        changes = 0
        for i in range(n):
            for j in range(n):
                if i in mark_row and j not in mark_col:
                    matrix[i][j] -= remain_min
                    changes += 1
                if i not in mark_row and j in mark_col:
                    matrix[i][j] += remain_min
                    changes += 1
        if changes == 0:
            raise Exception('No Change!')


if __name__ == '__main__':
    from mylib import StopWatch
    matrix = []
    with open('matrix.txt', 'r') as f:
        for line in f.readlines():
            matrix_line = []
            for i in range(len(line) // 4):
                matrix_line.append(int(line[4 * i:4 * i + 4]))
            matrix.append(matrix_line)

    test_matrix = [
        [7, 53, 183, 439, 863],
        [497, 383, 563, 79, 973],
        [287, 63, 343, 169, 583],
        [627, 343, 773, 959, 943],
        [767, 473, 103, 699, 303],
    ]

    with StopWatch():
        print(solve(matrix))

    with StopWatch():
        print(DPsolver(matrix))

    # n = len(matrix)
    # dict_matrix = dict()
    # for i in range(n):
    #     for j in range(n):
    #         dict_matrix[(i, j)] = -matrix[i][j]

    n = 15
    test_matrix = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            test_matrix[i][j] = -matrix[i][j]

    with StopWatch():
        matching = Munkres_slove(test_matrix)
        print(sum(matrix[i][matching[i] - n] for i in range(n)))
