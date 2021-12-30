from collections import Counter
from heapq import heappop, heappush


def compute(m, k):
    res = 0
    mem = Counter()
    cache = [(0, [0 for _ in range(k)])]
    mem[tuple(0 for _ in range(k))] = 1
    while cache:
        n, wall = heappop(cache)

        w = min(wall)
        idx = wall.index(w)

        for y in [2, 3]:
            s = wall[idx] + y
            tmp_wall = wall[:idx] + [s] + wall[idx + 1:]
            if tuple(tmp_wall) in mem:
                mem[tuple(tmp_wall)] += mem[tuple(wall)]
                continue

            if s == m:
                if all(ww == m for ww in tmp_wall):
                    res += mem[tuple(wall)]
                    break

            elif s > m:
                break

            elif (idx > 0 and wall[idx - 1] == s) or (idx < k - 1
                                                      and wall[idx + 1] == s):
                continue

            heappush(cache, (n + y, tmp_wall))
            mem[tuple(tmp_wall)] = mem[tuple(wall)]

    return res


if __name__ == "__main__":
    print(compute(9, 3))
    print(compute(32, 10))
