from numba import njit

mod = 999999937


@njit
def matrix_mul(A, B):
    C = [[0, 0], [0, 0]]
    C[0][0] = (A[0][0] * B[0][0] + A[0][1] * B[1][0]) % mod
    C[0][1] = (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % mod
    C[1][0] = (A[1][0] * B[0][0] + A[1][1] * B[1][0]) % mod
    C[1][1] = (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % mod
    return C


@njit
def matrix_pow(A, n):
    R = [[1, 0], [0, 1]]
    while n:
        if n & 1:
            R = matrix_mul(R, A)
        n >>= 1
        A = matrix_mul(A, A)

    return R


@njit
def pow(a, n):
    r = 1
    while n:
        if n & 1:
            r = r * a % mod
        n >>= 1
        a = a * a % mod
    return r


@njit
def compute(a, n):
    sq = int((a + 0.5)**0.5)
    if sq * sq == a:
        return pow(2 * sq, n)

    sq += 1

    A = [[2 * sq, a - sq * sq], [1, 0]]
    A = matrix_pow(A, n - 1)
    return (2 * (A[0][0] * sq + A[0][1]) - 1) % mod


@njit
def main(N):
    res = 0
    for a in range(1, N + 1):
        res += compute(a, a * a)
        res %= mod
    return res


if __name__ == '__main__':
    N = 5000000
    print(main(N))
