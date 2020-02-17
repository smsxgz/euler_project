from mylib import euler_prime, sqrt

N = 50000000
sq = sqrt(N)
primes = euler_prime(sq)

nums = set()
for a in primes:
    s1 = a**4
    if s1 >= N:
        break
    for b in primes:
        s2 = s1 + b**3
        if s2 >= N:
            break
        for c in primes:
            s3 = s2 + c**2
            if s3 >= N:
                break
            nums.add(s3)

print(len(nums))
