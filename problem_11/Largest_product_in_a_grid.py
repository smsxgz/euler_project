# -*- coding: utf-8 -*-
import collections
grid = []
with open('grid.txt', 'r') as f:
    for line in f.readlines():
        grid.append([int(s) for s in line.strip().split(' ')])


class node(collections.namedtuple('node', ['right', 'down', 'diag', 'ldiag'])):
    @property
    def max(self):
        return max(self.right, self.down, self.diag, self.ldiag)


def product_right(i, j, d):
    try:
        p = d[(i, j - 1)].right
    except KeyError:
        p = 0

    if j > 16:
        return 0
    a = grid[i][j - 1]
    if j == 0 or a == 0:
        return grid[i][j] * grid[i][j + 1] * grid[i][j + 2] * grid[i][j + 3]
    else:
        b = grid[i][j + 3]
        return p // a * b


def product_down(i, j, d):
    try:
        p = d[(i - 1, j)].down
    except KeyError:
        p = 0

    if i > 16:
        return 0
    a = grid[i - 1][j]
    if i == 0 or a == 0:
        return grid[i][j] * grid[i + 1][j] * grid[i + 2][j] * grid[i + 3][j]
    else:
        b = grid[i + 3][j]
        return p // a * b


def product_diag(i, j, d):
    try:
        p = d[(i - 1, j - 1)].diag
    except KeyError:
        p = 0

    if i > 16 or j > 16:
        return 0
    a = grid[i - 1][j - 1]
    if i == 0 or j == 0 or a == 0:
        return grid[i][j] * grid[i + 1][j + 1] * grid[i + 2][j + 2] *\
            grid[i + 3][j + 3]
    else:
        b = grid[i + 3][j + 3]
        return p // a * b


def product_ldiag(i, j, d):
    try:
        p = d[(i - 1, j + 1)].ldiag
    except KeyError:
        p = 0

    if i > 16 or j < 3:
        return 0
    if i == 0 or j == 19:
        return grid[i][j] * grid[i + 1][j - 1] * grid[i + 2][j - 2] *\
            grid[i + 3][j - 3]
    a = grid[i - 1][j + 1]
    if a == 0:
        return grid[i][j] * grid[i + 1][j - 1] * grid[i + 2][j - 2] *\
            grid[i + 3][j - 3]
    else:
        b = grid[i + 3][j - 3]
        return p // a * b


d = {}
m = 0
for i in range(20):
    for j in range(20):
        n = node(
            right=product_right(i, j, d),
            down=product_down(i, j, d),
            diag=product_diag(i, j, d),
            ldiag=product_ldiag(i, j, d))
        if m < n.max:
            m = n.max
        d[(i, j)] = n

print(m)
