from collections import defaultdict


def smallest_prime_factor(n):
    factor = [0] * (n + 1)
    prime = []

    for i in range(2, n + 1):
        if factor[i] == 0:
            factor[i] = i
            prime.append(i)

            for j in range(1, n // i + 1):
                if factor[j * i] == 0:
                    factor[j * i] = i
    return prime, factor


def factor_generator(fs):
    if len(fs) == 0:
        yield 1
        return

    p = fs[0]
    for m in factor_generator(fs[1:]):
        yield m
        yield p * m

    return


def main(N):
    prime, factor = smallest_prime_factor(N)
    prime = set(prime)

    res = []
    for p in prime:
        if (p + 3) // 2 not in prime:
            continue

        m = p - 1
        fs = []
        while m > 1:
            q = factor[m]
            if q in fs:
                break
            fs.append(q)
            m //= q

        else:
            for f in factor_generator(fs):
                if (p - 1) // f + f not in prime:
                    break
            else:
                res.append(p - 1)

    print(sum(res))


if __name__ == '__main__':
    from mylib import StopWatch

    with StopWatch():
        main(10**8)
