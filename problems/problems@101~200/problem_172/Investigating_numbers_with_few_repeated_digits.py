def generator(goal, d=10, path=[]):
    if goal == 0:
        yield path + [0] * d
        return

    if goal < 0 or goal > 3 * d:
        return

    if goal == 3 * d:
        yield path + [3] * d
        return

    for i in range(4):
        yield from generator(goal - i, d - 1, path + [i])
    return


factorials = dict()
factorials[0] = 1
for i in range(1, 19):
    factorials[i] = i * factorials[i - 1]

res = 0
for lst in generator(18):
    N = factorials[17] * (18 - lst[0])
    for n in lst:
        N //= factorials[n]
    res += N
print(res)
