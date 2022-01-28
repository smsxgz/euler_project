import math


def helper(n):
    theta = math.atan(math.sqrt(2 * n) / (n - 1)) - math.atan(1 / n)
    s1 = (1 - math.cos(theta) + math.sin(theta) - theta) / 2
    s2 = 1 - math.pi / 4
    return s1 / s2


def solver():
    l = 2000
    r = 3000
    while r - l > 1:
        mid = (l + r) // 2
        if helper(mid) > 0.001:
            l = mid
        elif helper(mid) < 0.001:
            r = mid
    return l, r


if __name__ == "__main__":
    print(solver())
