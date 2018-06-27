def available_nums(grid, x, y):
    nums = set(grid[(x, j)] for j in range(9)) | \
        set(grid[(i, y)] for i in range(9))

    nums |= set(grid[(x // 3 * 3 + i, y // 3 * 3 + j)]
                for i in range(3) for j in range(3))

    for m in range(1, 10):
        if m not in nums:
            yield m


def solve(grid, start=0):
    if all(v != 0 for v in grid.values()):
        yield grid
        return

    for i in range(start, 81):
        x, y = divmod(i, 9)
        if grid[(x, y)] == 0:
            for m in available_nums(grid, x, y):
                temp_grid = grid.copy()
                temp_grid[(x, y)] = m
                yield from solve(temp_grid, i + 1)
            return


def pprint(grid):
    for i in range(9):
        print(''.join([str(grid[(i, j)]) for j in range(9)]))


def main():
    with open('sudoku.txt', 'r') as f:
        res = 0
        while True:
            if f.readline():
                grid = {}
                for i in range(9):
                    for j, s in enumerate(f.readline().strip()):
                        grid[(i, j)] = int(s)
                g = next(solve(grid))
                res += 100 * g[(0, 0)] + 10 * g[(0, 1)] + g[(0, 2)]
            else:
                break
        print(res)


if __name__ == '__main__':
    # main()
    grid_str = [
        "300200000", "000107000", "706030500", "070009080", "900020004",
        "010800050", "009040301", "000702000", "000008006"
    ]

    grid = {}
    for i in range(9):
        for j, s in enumerate(grid_str[i]):
            grid[(i, j)] = int(s)

    for m in available_nums(grid, 0, 0):
        print(m)

    for g in solve(grid):
        pprint(g)
