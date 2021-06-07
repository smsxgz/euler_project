from mylib import euler_prime
import heapq

primes = euler_prime(10**7)
heapq.heapify(primes)
print(len(primes))


def solve(n):
    res = 1
    for _ in range(n):
        p = heapq.heappop(primes)
        heapq.heappush(primes, p**2)
        res *= p
        res %= 500500507
    return res


if __name__ == '__main__':
    print(solve(500500))
