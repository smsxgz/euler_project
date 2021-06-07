def solver(N):
    res = 0
    a = 1
    while a * (a + 1) <= N:
        res += N // a - a
        a += 1

    return res


if __name__ == "__main__":
    print(solver(10**6 // 4))
