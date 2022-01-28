def g(n):
    n = str(n)
    res = 0
    for k in range(1, len(n) + 1):
        if n[:k] == n[-k:]:
            res += 10**k
    return res - len(n) + 1


def p316():
    s = 0
    M = 10**16
    for n in range(2, 10**6):
        s += g(M // n)
    return s


if __name__ == "__main__":
    print(p316())
