from math import factorial

mem = dict()


def solve(f, n, m, k):
    # print(f, n, m, k)
    if m * f < k or k < m:
        return 0

    if f == 1:
        if m == k:
            return 1
        else:
            return 0

    if m == 0:
        return f ** n

    if (f, n, m, k) in mem:
        return mem[(f, n, m, k)]

    res = 0
    if m * f == k:
        for i in range(m, n + 1):
            c = factorial(n) // factorial(i) // factorial(n - i)
            res += c * solve(f - 1, n - i, 0, 0)

    else:
        for i in range((k - m) // (f - 1), -1, -1):
            c = factorial(n) // factorial(i) // factorial(n - i)
            res += c * solve(f - 1, n - i, m - i, k - f * i)
            print(f, res)

    mem[(f, n, m, k)] = res
    return res


if __name__ == "__main__":
    # print(solve(12, 20, 10, 70))
    print(solve(6, 5, 3, 15))
    # print(solve(3, 3, 1, 3))
