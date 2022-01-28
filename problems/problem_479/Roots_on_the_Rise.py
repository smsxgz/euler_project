from mylib import power_mod, inverse_mod

mod = 1000000007


def solve(n):
    r = 0
    for k in range(1, n + 1):
        m = inverse_mod(k * k, mod)
        r -= (power_mod(1 - k * k, n + 1, mod) - 1) * m + 1
        r %= mod
    print(r)


if __name__ == "__main__":
    solve(4)
    solve(10 ** 6)
