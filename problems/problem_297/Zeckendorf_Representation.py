from bisect import bisect_right

N = 10**17

fibo = [1, 2]
f = 2
while f < N:
    f = fibo[-1] + fibo[-2]
    fibo.append(f)

# f_n ~ f_{n+1} - 1
zeckendorf = [1, 1, 3]
for i in range(3, len(fibo)):
    zs = zeckendorf[i - 1] + zeckendorf[i - 2] + fibo[i - 3]
    zeckendorf.append(zs)


def solve(n):
    idx = bisect_right(fibo, n)
    res = sum(zeckendorf[:idx - 1])
    n -= fibo[idx - 1]

    while n > 0:
        idx = bisect_right(fibo, n)
        res += zeckendorf[idx]
        n -= fibo[idx - 1]
        res += n
    return res


if __name__ == '__main__':
    print(solve(N))
