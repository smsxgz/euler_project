table = {
    0: 1,
    1: 1,
    2: 2,
    3: 6,
    4: 24,
    5: 120,
    6: 720,
    7: 5040,
    8: 40320,
    9: 362880
}


def sum_factorial_digits(n):
    ssum = 0
    while n > 0:
        n, k = divmod(n, 10)
        ssum += table[k]
    return ssum


def compute(N=1000000):
    lst = [0] * N
    for i in range(1, N):
        if lst[i] > 0:
            continue
        chain = []
        m = i
        while m not in chain:
            chain.append(m)
            m = sum_factorial_digits(m)

        chain = chain[::-1]
        p = chain.index(m)

        for idx, mm in enumerate(chain):
            if mm >= N:
                continue
            if idx <= p:
                lst[mm] = p + 1
            else:
                lst[mm] = idx + 1

    longest = max(lst)
    num = 0
    for item in lst:
        if item == longest:
            num += 1
    return num


if __name__ == "__main__":
    print(compute())
