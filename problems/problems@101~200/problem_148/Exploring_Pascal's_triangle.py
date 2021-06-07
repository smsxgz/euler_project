def solve(N):
    lst = []
    while N > 0:
        lst.append(N % 7)
        N //= 7
    lst = lst[::-1]
    print(lst)

    n = len(lst)
    pre = 1
    res = 0
    for i in range(n):
        res += pre * (lst[i] * (lst[i] + 1) // 2) * 28**(n - i - 1)
        pre *= lst[i] + 1
    print(res + pre)


if __name__ == '__main__':
    N = 10**9 - 1
    solve(N)
