def compute(m):
    res = 1
    for i in range(1, m + 1):
        res *= (2 * i)**i
    return res // (m + 1)**(m * (m + 1) // 2)


if __name__ == "__main__":
    res = 0
    for m in range(2, 16):
        res += compute(m)
    print(res)
