import math
from mylib import euler_prime
from collections import defaultdict

zeta2 = 6 / (math.pi**2)


def solve():
    prime = euler_prime(1000000)
    m = len(prime)
    s = defaultdict(dict)
    for k in range(7):
        s[k + 1][m] = 0
    for i in range(m + 1):
        s[0][i] = 1

    for k in range(1, 8):
        for i in range(m - 1, -1, -1):
            s[k][i] = s[k][i + 1] + s[k - 1][i + 1] / (prime[i]**2 - 1)

    return zeta2 * s[7][0]


# or compute by this way:
# 6 (s1^7 - 21 s1^5 s2 + 105 s1^3 s2^2 - 105 s1 s2^3 + 70 s1^4 s3 -
# 420 s1^2 s2 s3 + 210 s2^2 s3 + 280 s1 s3^2 - 210 s1^3 s4 + 630 s1 s2 s4 -
# 420 s3 s4 + 504 s1^2 s5 - 504 s2 s5 - 840 s1 s6 + 720 s7)/(5040 Pi^2)
