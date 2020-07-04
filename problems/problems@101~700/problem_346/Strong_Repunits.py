import math
from mylib import sqrt


def solve(N):
    check = set()
    ans = 0
    for base in range(2, sqrt(N)):
        base_i = 1 + base + base * base
        while True:
            if base_i >= N:
                break
            if base_i not in check:
                check.add(base_i)
                ans += base_i
            base_i = 1 + base * base_i
    return ans + 1


# https://en.wikipedia.org/wiki/Goormaghtigh_conjecture
def solve2(N):
    ans = 0
    for base in range(2, sqrt(N) + 1):
        m = int(math.log(N, base)) + 1
        mbase = base**m
        while True:
            if (mbase - 1) < (base - 1) * N:
                break
            m -= 1
            mbase //= base
        if m <= 2:
            break
        ans += ((base * mbase - base**3) // (base - 1) - m + 2) // (base - 1)

    if N > 31:
        ans -= 31
    if N > 8191:
        ans -= 8191
    return ans + 1


def is_111(n):
    "Returns true iff n can be expressed as 111 in some (integer) base"
    r = sqrt(4 * n - 3)
    return (r * r) == (4 * n - 3) and (r & 1) != 0


def sum_1111(limit):
    # First, compute sum of short (111 and 1) strong repunits
    b = (sqrt(4 * limit - 3) - 1) // 2
    short_sum = 1 + (((b + 3) * b + 5) * b - 9) // 3

    # Now, compute and sum repunits, but only those with 4 digits or more.
    rep_set = set()
    max_base = int((limit + 0.5)**(1 / 3))

    for b in range(2, int(max_base) + 1):
        rep = ((b + 1) * b + 1) * b + 1  # 1111 in base b
        while rep <= limit:
            if not is_111(rep):
                rep_set.add(rep)
            rep = rep * b + 1
    return sum(rep_set) + short_sum


if __name__ == '__main__':
    from mylib import StopWatch
    # solve(1000)
    with StopWatch():
        print(solve(10**12))

    with StopWatch():
        print(solve2(10**12))

    with StopWatch():
        print(sum_1111(10**12))
