from mylib import euler_prime

N = 10**8
prime = euler_prime(N // 2)

count = 0
for i in range(len(prime)):
    for j in range(i, len(prime)):
        if prime[i] * prime[j] < N:
            count += 1
        else:
            break
print(count)
