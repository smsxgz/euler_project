def lst2num(lst):
    res = 0
    for i in lst:
        res = 2 * res + i
    return res


def dfs(seq=[1, 0, 0, 0, 0, 0, 1], nums=[0, 1, 16]):
    if len(seq) == 32:
        lsts = [
            seq[-4:] + [1], seq[-3:] + [1, 0], seq[-3:] + [1, 0],
            seq[-2:] + [1, 0, 0], seq[-1:] + [1, 0, 0, 0]
        ]
        for lst in lsts:
            if lst2num(lst) in nums:
                return

        yield seq[1:] + [1]
        return

    for i in [0, 1]:
        s = lst2num(seq[-4:] + [i])
        if s not in nums:
            yield from dfs(seq + [i], nums + [s])


if __name__ == '__main__':
    res = 0
    for seq in dfs():
        res += lst2num(seq)
    print(res)
