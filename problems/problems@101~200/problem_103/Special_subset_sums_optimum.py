d = 7
S = (d - 1) * 2**(d - 1) + 1


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


def find(n, path, sums):
    if n == 0:
        yield path
        return

    m = path[-1] + 1
    SS = S - sum(path)
    while n * m + n * (n - 1) // 2 < SS:
        if helper(path + [m]):
            tmp_sums = sums.copy()
            if allsums(tmp_sums, m):
                yield from find(n - 1, path + [m], tmp_sums)
        m += 1


if __name__ == "__main__":
    optimal_set_sum = S
    optimal_set = None
    for a in range(1, S // d):
        for b in range(a + 1, S // d + 1):
            for solution in find(d - 2, [a, b], {a, b, a + b}):
                if sum(solution) < optimal_set_sum:
                    optimal_set_sum = sum(solution)
                    optimal_set = solution

    print(optimal_set_sum, optimal_set)
