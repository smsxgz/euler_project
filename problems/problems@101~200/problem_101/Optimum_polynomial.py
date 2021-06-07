Combinations = {(1, 0): 1, (1, 1): 1}
for i in range(2, 11):
    for j in range(i + 1):
        if j == 0 or j == i:
            Combinations[(i, j)] = 1
        else:
            Combinations[(
                i,
                j)] = Combinations[(i - 1, j - 1)] + Combinations[(i - 1, j)]


def BOP(k, seq):
    res = 0
    for i in range(1, k + 1):
        t = Combinations[(k, i - 1)] * seq[i]
        if (k - i) % 2 == 1:
            t = -t
        res += t
    return res


def compute(seq, degree):
    res = 0
    for k in range(1, degree + 1):
        t = BOP(k, seq)
        print(t)
        res += t

    return res


if __name__ == "__main__":

    def poly(n):
        res = 0
        for i in range(11):
            res = res * n + 1 - 2 * (i % 2)
        return res

    seq = []
    for i in range(12):
        seq.append(poly(i))

    # seq = [0, 1, 8, 27, 64, 125]
    print(compute(seq, 10))
