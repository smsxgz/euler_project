from mylib import inverse_mod, power_mod

mod = 1020202009
p = inverse_mod(2, mod)


def solver(n):
    c = [1]
    for i in range(n-2):
        c = [0] + c + [0]
        cc = []
        for j in range(i + 3, 0, -2):
            idx = (i + 3 - j) // 2
            cc.append((c[idx] * (j + 1) + c[idx + 1] * (j-1)) % mod)
        c = cc
    
    res = 0
    for j in range(n, 0, -2):
        idx = (n - j) // 2
        res = (res + c[idx] * j) % mod
    return (res * power_mod(p, n-1, mod)) % mod


def solver2(n):
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    dp[n][0] = 1
    for i in range(n-1, -1, -1):
        for j in range(min(i+1, n - i + 1)):
            dp[i][j] = dp[i+1][j]
            if j < n:
                dp[i][j] += (j + 1) * dp[i+1][j+1]
            if j > 0:
                dp[i][j] += (n - i - j) * dp[i+1][j - 1]
            dp[i][j] %= mod

    return dp[0][0]


if __name__ == "__main__":
    from mylib import StopWatch
    with StopWatch():
        print(solver2(24680))

    # with StopWatch():
    #     print(solver(24680))
