path = [[list(range(1, i + 1))] for i in range(201)]
for i in range(1, len(path)):
    for j in path[i]:
        for k in [a for a in j if i + a < len(path)]:
            if len(path[i][0]) + 1 < len(path[i + k][0]):
                path[i + k] = [j + [i + k]]
            elif len(path[i][0]) + 1 == len(path[i + k][0]):
                path[i + k].append(j + [i + k])
print(sum(len(p[0]) - 1 for p in path[1:]))
