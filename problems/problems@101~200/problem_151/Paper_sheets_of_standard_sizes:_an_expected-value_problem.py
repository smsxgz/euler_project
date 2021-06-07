from fractions import Fraction

mem = dict()
mem[(1)] = 1


def helper(lst):
    if lst in mem:
        return mem[lst]

    if len(lst) == 0:
        return 0

    n = len(lst)
    p = Fraction(1, n)
    res = (n == 1)
    for i in range(n):
        tmp_lst = list(lst)
        m = tmp_lst.pop(i)
        while m > 1:
            m //= 2
            tmp_lst.append(m)
        tmp_lst.sort()
        res += p * helper(tuple(tmp_lst))

    mem[lst] = res
    return res


if __name__ == '__main__':
    print(helper((16, )))
