from math import log, e
from mylib import gcd


def is_terminating(q, p):
    d = gcd(q, p)
    p = p // d

    while p % 2 == 0:
        p //= 2
    while p % 5 == 0:
        p //= 5

    return p == 1


def maximum_product(n):
    k = int(n / e)
    if k * (log(n) - log(k)) > (k + 1) * (log(n) - log(k + 1)):
        return k
    else:
        return k + 1


def compute(n):
    res = 0
    for i in range(5, n + 1):
        k = maximum_product(i)
        if is_terminating(i, k):
            res -= i
        else:
            res += i

    return res


if __name__ == "__main__":
    print(compute(10000))
