import numpy as np


def generate_transition_matrix(n):
    m = n * n
    matrix = np.zeros((m, m))
    for s in range(m):
        i, j = divmod(s, n)
        c = 0
        for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ix, jy = i + x, j + y
            if ix >= 0 and ix < n and jy >= 0 and jy < n:
                c += 1
                matrix[s, n * ix + jy] = 1
        matrix[s] /= c

    return matrix


def solver(n, k):
    P = generate_transition_matrix(n)
    Q = np.linalg.matrix_power(P, k)
    return np.prod(1 - Q, axis=0).sum()


if __name__ == "__main__":
    s = solver(30, 50)
    print(s)
