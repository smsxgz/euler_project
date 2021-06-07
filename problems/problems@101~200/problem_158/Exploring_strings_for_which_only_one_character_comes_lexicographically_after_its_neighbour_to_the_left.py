factorial = {1: 1}
for i in range(2, 27):
    factorial[i] = factorial[i - 1] * i


def compute(n):
    p = 1
    for i in range(26, 26 - n, -1):
        p *= i

    p //= factorial[n]
    p *= 2**n - n - 1

    return p


def main():
    max_p = 0
    for n in range(2, 27):
        max_p = max(max_p, compute(n))
    print(max_p)


if __name__ == '__main__':
    main()
