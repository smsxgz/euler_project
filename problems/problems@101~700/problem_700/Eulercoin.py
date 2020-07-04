from mylib import extend_Eulid


def solution(k, m):
    k1, *_ = extend_Eulid(k, m)
    k1 = m - (k1 % m)  # -k1 * k % m = 1

    ssum = k
    pre_coin = k
    n = k
    count = 1
    while True:
        n = (n + k) % m
        if n < pre_coin:
            ssum += n
            pre_coin = n
            count += 1
        if count == 15:
            break

    table = [k1]
    for _ in range(pre_coin - 1):
        table.append((table[-1] + k1) % m)

    while pre_coin > 1:
        pre_coin -= (-min(table[:pre_coin]) * k) % m
        ssum += pre_coin

    return ssum


def helper(A, M, L, R):
    # find minimum x such that L <= Ax(mod M) <= R
    # (A, M) = 1

    if A > M:
        A = A % M

    t = (L - 1) // A + 1
    if t * A <= R:
        return t
    else:
        _, r = divmod(-M, A)
        x = helper(r, A, L % A, R % A)

        x = (x * M + L - 1) // A + 1

    # print(f'{L} <= {A}*{x}(mod {M}) <= {R}')
    return x


def solution2(k, m):
    ssum = k
    pre_coin = k
    while pre_coin > 1:
        x = helper(k, m, 1, pre_coin - 1)
        pre_coin = (x * k) % m
        ssum += pre_coin
    return ssum


def solution3(k, m):
    ssum = k
    lo = hi = k
    while lo > 0:
        mid = (lo + hi) % m
        if mid < lo:
            lo = mid
            ssum += lo
        else:
            hi = mid
    return ssum


def solution4(k, m):
    pre_index, pre_coin = 1, k
    index, coin = 3, (3 * k) % m
    ssum = pre_coin + coin

    while True:
        pre_index, index = index, (
            (pre_coin - 1) // coin + 1) * index - pre_index
        pre_coin, coin = coin, (-pre_coin) % coin
        ssum += coin
        if coin == 1:
            break
    return ssum


if __name__ == '__main__':
    from mylib import StopWatch

    k = 1504170715041707
    m = 4503599627370517

    with StopWatch():
        print(solution2(k, m))

    with StopWatch():
        print(solution3(k, m))

    with StopWatch():
        print(solution4(k, m))
