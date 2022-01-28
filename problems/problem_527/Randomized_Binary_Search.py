import numpy as np

mem = dict()
mem[0] = 0
mem[1] = 1


def binary(n):
    if n in mem:
        return mem[n]

    mid = (1 + n) // 2
    res = n + binary(mid - 1) + binary(n - mid)
    mem[n] = res
    return res


def random_binary(n):
    return 2 * (n + 1) / n * (np.log(n) + 0.57721566490153) - 3


if __name__ == "__main__":
    N = 10**10
    print(random_binary(N) - binary(N) / N)
