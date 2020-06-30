from collections import defaultdict
from mylib import gcd


def main(L):
    A = int((L // 2 + 0.5)**0.5)

    cache = defaultdict(int)
    a = 1
    while True:
        for b in range(2, A + 1, 2):
            m = 2 * a * b + 2 * max(a * a, b * b)
            if m > L:
                break

            if gcd(a, b) == 1:
                for i in range(1, L // m + 1):
                    cache[i * m] += 1
        a += 2
        if a > A:
            break

    res = 0
    for m in cache:
        if cache[m] == 1:
            res += 1
    print(res)


if __name__ == '__main__':
    # main(12)
    from mylib import StopWatch

    with StopWatch():
        main(1500000)
