from mylib import euler_prime

prime = euler_prime(10**4)
m = len(prime)

table = [[1 for _ in range(m + 1)], [0 for _ in range(m + 1)]]

n = 2
while True:
    t = [0 for _ in range(m + 1)]
    for i in range(m - 1, -1, -1):
        if n >= prime[i]:
            t[i] = table[n - prime[i]][i] + t[i + 1]
    table.append(t)

    if table[-1][0] > 5000:
        print(n)
        break

    n += 1
