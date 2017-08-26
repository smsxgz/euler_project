mod = 10**10


def pow2(n):
    if n == 1:
        return 2
    m = pow2(n // 2)
    if n % 2 == 1:
        return (m * m * 2) % mod
    else:
        return (m * m) % mod


(pow2(7830457) * 28433) % mod + 1
