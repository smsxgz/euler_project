from mylib import euler_prime

row = 51
primes = euler_prime(row - 1)

factors = [[0 for _ in range(len(primes))] for _ in range(row)]

for i in range(2, row):
    for j, p in enumerate(primes):
        q = i
        while q >= p:
            q //= p
            factors[i][j] += q


def Binomial(n, k):
    res = 1
    for j, p in enumerate(primes):
        a = factors[n][j] - factors[k][j] - factors[n - k][j]
        res *= p**a
    return res


squarefree = set()
for i in range(2, row):
    for j in range(1, i // 2 + 1):
        for k in range(len(primes)):
            if factors[i][k] - factors[j][k] - factors[i - j][k] >= 2:
                break
        else:
            squarefree.add(Binomial(i, j))

print(sum(squarefree) + 1)
