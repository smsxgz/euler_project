# from collections import defaultdict
from mylib import gcd
mod = 10**9


def solver(N):
    res = 11
    P = int((N + 1)**(1 / 4))

    for p in range(2, P):
        q0 = p % 2 + 1
        for q in range(q0, p, 2):
            if gcd(p, q) != 1:
                continue

            x, y = p * p - q * q, 2 * p * q
            c = p * p + q * q

            a, b = 3 * x + 2 * y, abs(2 * x - 3 * y)
            if a * c <= N and a * b <= N and a % 13 != 0:
                res += a * b + a * c + b * c
                res %= mod

            a, b = 2 * x + 3 * y, abs(3 * x - 2 * y)
            if a * c <= N and a * b <= N and a % 13 != 0:
                res += a * b + a * c + b * c
                res %= mod

    return res


if __name__ == "__main__":
    from mylib import StopWatch

    with StopWatch():
        print(solver(10**16))
