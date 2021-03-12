def counting(prime_list, N):
    if len(prime_list) == 0:
        # print(f)
        return 1

    p = prime_list[0]
    res = 0
    q = 1
    while q <= N:
        res += counting(prime_list[1:], N // q)
        q *= p
    return res


if __name__ == "__main__":
    from mylib import euler_prime, StopWatch

    primes = euler_prime(100)
    with StopWatch():
        print(counting(primes, 10**9))
