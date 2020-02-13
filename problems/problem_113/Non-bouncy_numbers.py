def increasing_number(n):
    c = 1
    res = 0
    for i in range(n):
        c = c * (9 + i) // (i + 1)
        res += c
    return res


def decreasing_number(n):
    c = 1
    res = 0
    for i in range(n):
        c = c * (10 + i) // (i + 1)
        res += c
    return res - n


def non_bouncy(n):
    return increasing_number(n) + decreasing_number(n) - 9 * n


if __name__ == "__main__":
    print(non_bouncy(6))
    print(non_bouncy(10))
    print(non_bouncy(100))
