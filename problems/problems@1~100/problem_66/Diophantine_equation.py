# fundamental solution of Pell's Equation
from mylib import sqrt


def continued_fraction(n):
    sq = sqrt(n)
    if sq * sq == n:
        return [sq]

    # (\sqrt{n} + b) / c
    b, c = 0, 1
    fraction = []

    while True:
        a = (sq + b) // c
        fraction.append(a)

        r = n - (a * c - b)**2
        assert r % c == 0

        b = a * c - b
        c = r // c

        if c == 1:
            return fraction + [sq + b]


def solve(n):
    sq = sqrt(n)
    if sq * sq == n:
        return None

    n0, *cycle = continued_fraction(n)

    pre_h, pre_k = 1, 0
    h, k = n0, 1
    idx = 0
    while True:
        if h**2 - n * k**2 == 1:
            return h, k

        a = cycle[idx % len(cycle)]
        h, k, pre_h, pre_k = a * h + pre_h, a * k + pre_k, h, k
        idx += 1


if __name__ == '__main__':
    h_max = -1
    res = -1
    for i in range(2, 1001):
        solution = solve(i)
        if solution:
            if solution[0] > h_max:
                h_max = solution[0]
                res = i
    print(res)
