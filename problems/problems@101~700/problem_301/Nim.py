def solve(n):
    a, b = 1, 0
    for i in range(n):
        a, b = a + b, a
    return a + b


if __name__ == "__main__":
    print(solve(30))
