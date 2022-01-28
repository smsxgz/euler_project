N = 10 ** 13

fibo = [1, 2]
f = 2
while f <= N:
    f = fibo[-1] + fibo[-2]
    fibo.append(f)

fibo.append(fibo[-1] + fibo[-2])


def solve(n, k):
    if n == 0:
        return 1

    if n >= fibo[k + 2] - 2:
        return 2 ** (k + 1)

    r = solve(n, k - 1)
    if n >= fibo[k]:
        r += solve(n - fibo[k], k - 1)
    return r


if __name__ == "__main__":
    print(solve(N, len(fibo) - 3))
