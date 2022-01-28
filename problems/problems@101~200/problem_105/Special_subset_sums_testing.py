def helper(path):

    k = (len(path) - 1) // 2
    s = path[0]
    for i in range(1, k + 1):
        s += path[i] - path[-i]
        if s <= 0:
            return False
    return True


def allsums(sums, m):
    for s in list(sums):
        if s + m in sums:
            return False
        sums.add(s + m)
    sums.add(m)
    return True


def test(path):
    path.sort()

    if not helper(path):
        return False

    sums = {path[0], path[1], path[0] + path[1]}
    for m in path[2:]:
        if not allsums(sums, m):
            return False
    # print(path)

    return True


if __name__ == "__main__":
    with open('p105_sets.txt', 'r') as f:
        res = 0
        for line in f.readlines():
            path = [int(s) for s in line.strip().split(',')]
            if test(path):
                res += sum(path)
        print(res)
