from collections import defaultdict
from mylib import sqrt

n = 12000
# 1 * (k - 2) + 2 + k = 1^(k-2) * 2 * k
limits = 2 * n

factors = defaultdict(list)
for d in range(2, sqrt(limits)):
    for i in range(d, limits // d + 1):
        factors[i * d].append(d)

min_product_sum = [2 * i for i in range(n + 1)]


def factorize(m, min_factor=None, terms=[]):
    if len(factors[m]) == 0:
        # yield terms + [m]
        return

    if min_factor is None:
        min_factor = factors[m][0]

    for d in factors[m]:
        if d < min_factor:
            continue
        yield terms + [d, m // d]
        yield from factorize(m // d, d, terms + [d])
    return


def main():
    for m in range(4, limits + 1):
        for terms in factorize(m):
            c = m - sum(terms) + len(terms)
            if c > n:
                continue
            if min_product_sum[c] > m:
                min_product_sum[c] = m
    print(sum(set(min_product_sum[2:])))


if __name__ == '__main__':
    main()
