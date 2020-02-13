from mylib import euler_func


def count(n):
    res = [0] * 10
    while n > 0:
        n, r = divmod(n, 10)
        res[r] += 1
    return res


def is_permutation(n, m):
    return count(n) == count(m)


phis = euler_func(9999999)

min_ratio = 2.
min_index = -1
for n, phi in enumerate(phis):
    if n < 2:
        continue

    if is_permutation(n, phi):
        if n / phi < min_ratio:
            min_ratio = n / phi
            min_index = n

print(min_index)
