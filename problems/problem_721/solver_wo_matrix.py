from numba import njit

mod = 999999937


@njit
def pow(a, n):
    r = 1
    while n:
        if n & 1:
            r = r * a % mod
        n >>= 1
        a = a * a % mod
    return r


@njit
def nth(n, a0, a1, x, y):
    # find n-th term from linear recurrence: a(n) = x * a(n-1) + y * a(n-2)
    # with initial term a(0) = a0, a(1) = a1

    while n > 1:
        if n & 1:
            a1, a0 = ((x * x + y) % mod * a1 + (x * y) % mod * a0) % mod, a1
        else:
            a1 = (x * a1 + y * a0) % mod
        x = (x * x + 2 * y) % mod
        y = mod - y * y % mod
        n >>= 1
    return a1


@njit
def compute(a, n):
    sq = int((a + 0.5)**0.5)
    if sq * sq == a:
        return pow(2 * sq, n)

    sq += 1

    return nth(n, 2, 2 * sq, 2 * sq, a - sq * sq) - 1


@njit
def main(N):
    res = 0
    for a in range(1, N + 1):
        res += compute(a, a * a)
        res %= mod
    return res


if __name__ == '__main__':
    N = 5000000
    print(main(N))
