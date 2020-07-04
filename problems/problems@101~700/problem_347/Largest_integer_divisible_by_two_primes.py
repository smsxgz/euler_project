from math import log
from mylib import euler_prime, StopWatch


def solve(N):
    prime = euler_prime(N // 2)
    m = len(prime)
    res = 0
    for i in range(m - 1):
        p = prime[i]
        log_p = int(log(N + 0.5, p))
        for j in range(i + 1, m):
            q = prime[j]
            if p * q > N:
                break
            M = 0
            ppow = 1
            for pow in range(1, log_p + 1):
                ppow *= p
                qow = int(log(N // ppow + 0.5, q))
                if qow < 1:
                    continue
                else:
                    M = max(M, ppow * q**qow)
            res += M

    return res


N = 10000000
with StopWatch():
    print(solve(N))
