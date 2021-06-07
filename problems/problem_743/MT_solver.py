from numba import jit
import time


# Montgomery batch inversion...
@jit(nopython=True)
def batch_inversion(v, MOD):
    N = len(v)
    c = 1
    t = [0] * N
    for i in range(N):
        t[i] = c
        c = (c * v[i]) % MOD
    c = pow2(c, MOD - 2, MOD)
    i = N - 1
    while i >= 0:
        t[i] = (c * t[i]) % MOD
        c = (c * v[i]) % MOD
        i -= 1

    return t


# Does the same as pow(b,e,m) in Python3, but also can run with Numba
@jit(nopython=True)
def pow2(x, e, m):
    X = x
    E = e
    Y = 1
    while E > 0:
        if E % 2 == 0:
            X = (X * X) % m
            E = E / 2
        else:
            Y = (X * Y) % m
            E = E - 1
    return Y


@jit(nopython=True)
def run(n=10**16, k=10**8, MOD=1000000007):
    pow_4 = pow2(4, n // 2, MOD)  # starting value which is 4^(n/2)
    div_4 = pow2(pow2(4, MOD - 2, MOD), n // k,
                 MOD)  # compute the modular inverse of 4^(n/k)

    seq_inv = list(range(
        1,
        k // 2 + 2))  # last value is unneccessary, but required in the loop...
    seq_inv = batch_inversion(seq_inv, MOD)

    q = 1  # for i=k/2
    r = k
    S = 0
    for i in range(0, k // 2 + 1):  # start with i =k/2
        S += (q * pow_4) % MOD
        S %= MOD

        # for next iteration:
        q = (q * r) % MOD
        q = (q * (r - 1)) % MOD
        q = (q * pow2(seq_inv[i], 2, MOD)) % MOD
        r -= 2

        # divide pow_4 by 4^(n/k)
        pow_4 = (pow_4 * div_4) % MOD

    return S


start = time.time()
S = run()
print("Time:", time.time() - start)
print("Solution", S)
