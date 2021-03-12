from mylib import Miller_Rabin


def generator(n, d, m, prefix=[]):
    if n == m:
        yield prefix + [d] * m
        return

    if n == 0:
        yield prefix
        return

    for i in range(10):
        if i != d:
            yield from generator(n - 1, d, m, prefix + [i])
        else:
            yield from generator(n - 1, d, m - 1, prefix + [i])


def lst2num(lst):
    res = 0
    for i in lst:
        res = 10 * res + i
    return res


def find_prime(n, d, m):
    res = []
    for lst in generator(n, d, m):
        if lst[0] == 0:
            continue
        p = lst2num(lst)
        if Miller_Rabin(p):
            res.append(p)

    return sum(res)


res = 0
for i in range(10):
    m = 9
    r = 0
    while r == 0:
        r = find_prime(10, i, m)
        m -= 1
    res += r

print(res)
