from collections import Counter, defaultdict

mem = defaultdict(Counter)


def bfs(k, base):
    cache = [
        [],
    ]
    while cache:
        p = cache.pop(-1)
        i = len(p)
        colors = set()
        if len(base) < k:
            if i < k - 1:
                colors.add(base[i])
            if i > 0:
                colors.add(base[i - 1])
        else:
            colors.add(base[i])

        for c in set([0, 1, 2]) - colors:
            pp = p + [c]
            if i == k - 1:
                if len(base) < k:
                    mem[2 * k][tuple(p + [c])] += mem[2 * k - 1][base]
                else:
                    mem[2 * k + 1][tuple(p + [c])] += mem[2 * k][base]
            else:
                cache.append(pp)


mem[2][(0, )] = 1
mem[2][(1, )] = 1
mem[2][(2, )] = 1

for i in range(1, 8):
    for base in mem[2 * i]:
        bfs(i, base)

    for base in mem[2 * i + 1]:
        bfs(i + 1, base)

print(mem.keys())
print(sum(mem[16].values()))
