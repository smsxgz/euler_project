from mylib import gcd


def rad(n):
    res = [1] * n

    for i in range(2, n):
        if res[i] == 1:
            for m in range(i, n, i):
                res[m] *= i

    return res


def solver(n):
    rad_list = rad(n)
    rad_sort = sorted((rad_list[i], i) for i in range(1, n))

    res = 0
    for c in range(4, n):

        k = c // rad_list[c]
        for rada, a in rad_sort:
            if rada > k // 2:
                break
            if a > c // 2:
                continue

            b = c - a
            if rada * rad_list[b] < k and gcd(a, b) == 1:
                res += c
    print(res)


if __name__ == "__main__":
    solver(1000)
    solver(120000)
