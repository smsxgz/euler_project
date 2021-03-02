from mylib import StopWatch

with StopWatch():
    N = 10**7
    lst = [2] * (N + 1)

    D = int(N**0.5)
    for d in range(2, D + 1):
        lst[d * d] += 1
        for m in range(d + 1, N // d + 1):
            lst[d * m] += 2

    count = 0
    for i in range(2, N):
        if lst[i] == lst[i + 1]:
            count += 1
            # print(i - 1)

    print(count)
