from mylib import sqrt


def is_prime(x):
    if x <= 1:
        return False
    elif x <= 3:
        return True
    elif x % 2 == 0:
        return False
    else:
        for i in range(3, sqrt(x) + 1, 2):
            if x % i == 0:
                return False
        return True


def solve():
    res = 0
    d = 1
    s = 1
    while True:
        for _ in range(3):
            s += 2 * d
            if is_prime(s):
                res += 1
        s += 2 * d
        if 10 * res < (4 * d + 1):
            print(2 * d + 1)
            return 2 * d + 1
        d += 1


if __name__ == "__main__":
    solve()
