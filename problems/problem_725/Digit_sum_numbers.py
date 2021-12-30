from mylib import inverse_mod

mod = 10**16

n = 2020
# n = 7
binom = [[0 for _ in range(10)] for _ in range(n + 9)]
for i in range(n + 9):
    binom[i][0] = 1
    for j in range(1, 10):
        binom[i][j] = binom[i - 1][j - 1] + binom[i - 1][j]


def helper(nums):
    k = len(nums)
    res = [[0 for _ in range(10)] for _ in range(k + 1)]

    for m in range(10):
        res[1][m] = m * nums[0]

    for i in range(2, k + 1):
        a = nums[i - 1]
        for M in range(1, 10):
            for m in range(M + 1):
                res[i][M] += (M - m) * binom[m + i - 2][m] * a
                res[i][M] += res[i - 1][m]

    return res[-1]


def main():
    nums = []
    for i in range(n - 1):
        if i < 16:
            nums.append(((n - 1 - i) * 10**i + (i + 1) * 10**(i + 1)) % mod)
        else:
            nums.append(0)

    h = helper(nums)
    # print(nums, h)
    res = 0
    N = -1 * inverse_mod(9, mod)

    for m in range(1, 10):
        res += N * m * binom[m + n - 2][m] + h[m]
        res %= mod

    res -= 45 * N * (n - 1)
    res %= mod

    print(res)


if __name__ == "__main__":
    main()
