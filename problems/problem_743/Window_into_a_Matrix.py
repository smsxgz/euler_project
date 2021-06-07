from mylib import inverse_mod, power_mod

mod = 1000000007


def solver(k, m):
    A = power_mod(2, k * m, mod)
    C = 1
    res = C * A

    B = inverse_mod(power_mod(2, 2 * m, mod), mod)

    for i in range(2, k + 1, 2):
        # if i % 1000000 == 0:
        #     print(i)

        A *= B
        A %= mod

        C *= ((k - i + 2) % mod) * ((k - i + 1) % mod)
        C *= inverse_mod(i // 2, mod)**2
        C %= mod

        res += C * A
        # print(C, A, res)
        res %= mod

    return res


if __name__ == '__main__':
    from time import perf_counter
    time1 = perf_counter()
    print(solver(10**8, 10**8))
    time2 = perf_counter()
    print('Time =', time2 - time1)
