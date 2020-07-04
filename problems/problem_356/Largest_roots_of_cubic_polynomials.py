mod = 10**8
K = 987654321


def matrix_mul(A, B):
    C = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % mod
    return C


def matrix_pow(A, k):
    R = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    while k:
        if k & 1:
            R = matrix_mul(R, A)
        k >>= 1
        A = matrix_mul(A, A)
    return R


def main():
    res = 0
    for i in range(1, 31):
        p = (2**i) % mod
        A = [[p, 0, -i % mod], [1, 0, 0], [0, 1, 0]]
        B = matrix_pow(A, K - 2)
        res += B[0][0] * p**2 % mod + B[0][1] * p % mod + B[0][2] * 3 % mod - 1
        res %= mod
    print(res)


if __name__ == '__main__':
    main()
