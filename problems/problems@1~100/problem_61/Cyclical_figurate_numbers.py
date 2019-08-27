from addict import Dict


def polygonal(n, poly=3):
    return n * ((poly - 2) * n - (poly - 4)) // 2


cache = Dict()
for pw in range(3, 9):
    for i in range(1, 200):
        poly = polygonal(i, pw)
        if poly < 1000:
            continue
        if poly > 10000:
            break
        if cache[poly // 100][pw]:
            cache[poly // 100][pw].append(poly % 100)
        else:
            cache[poly // 100][pw] = [poly % 100]


def solve(path, unused):
    if len(path) == 6:
        if path[-1][1] == path[0][0]:
            yield path
            return

    candidate = cache[path[-1][1]]
    for pw in unused:
        tmp_unused = unused.copy()
        tmp_unused.remove(pw)
        for j in candidate[pw]:
            yield from solve(path + [(path[-1][1], j)], tmp_unused)


for i in range(100):
    unused = set([3, 4, 5, 6, 7, 8])
    for pw in cache[i]:
        tmp_unused = unused.copy()
        tmp_unused.remove(pw)
        for j in cache[i][pw]:
            for p in solve([(i, j)], tmp_unused):
                print(p)
                res = 0
                for x, y in p:
                    res += 100 * x + y
                print(res)
