mod = 1000000007
table = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]


def power(n, k):
    if k == 0:
        return 1
    elif k == 1:
        return n % mod

    m = power(n, k // 2)
    if k % 2 == 1:
        return (m * m * n) % mod
    else:
        return (m * m) % mod


def sum_inverse_digit_sum(n):
    q, r = divmod(n, 9)
    p = power(10, q)
    res = (6 + table[r] + r) * p - 6 - 9 * q - r
    return res % mod


fibo = [0, 1, 1]
ssum = 1
for i in range(3, 91):
    fibo.append(fibo[-1] + fibo[-2])
    ssum += sum_inverse_digit_sum(fibo[-1])
    ssum %= mod
print(ssum)
