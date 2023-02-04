def compute(n, k):
    return k * k * n * (4 * k * n + n + 2 * k - 4) / (3 * (n * k + k - 1))


if __name__ == "__main__":
    print(compute(2, 2))
    print(compute(10 ** 6, 10))
