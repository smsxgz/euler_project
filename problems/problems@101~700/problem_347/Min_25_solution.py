from math import sqrt


def prob347(N):
    def isqrt(n):
        if n <= 0:
            return 0

        x = int(sqrt(n) * (1 + 1e-12))
        while True:
            y = (x + n // x) >> 1
            if y >= x:
                return x
            x = y

    def icbrt(n):
        if n <= 0:
            return 0

        x = int(n**(1. / 3.) * (1 + 1e-12))
        while True:
            y = (2 * x + n // (x * x)) // 3
            if y >= x:
                return x
            x = y

    def prime_sieve(N):
        if N < 2:
            return []

        size = (N + 1) // 2
        is_prime = [1] * size
        is_prime[0] = 0
        v = int(N**0.5) // 2 + 1
        for p in range(1, v):
            if not is_prime[p]:
                continue
            for k in range(2 * p * (p + 1), size, 2 * p + 1):
                is_prime[k] = 0

        primes = [2]
        primes.extend([2 * p + 1 for p in range(1, size) if is_prime[p]])
        return primes

    def tabulate_all_primes_sum(N):
        def T(n):
            return n * (n + 1) // 2 - 1

        if N <= 1:
            return ValueError(N)

        v = isqrt(N)
        smalls = [T(i) for i in range(v + 1)]
        larges = [0 if i == 0 else T(N // i) for i in range(v + 1)]

        for p in range(2, v + 1):
            if smalls[p - 1] == smalls[p]:
                continue
            p_sum = smalls[p - 1]
            q = p * p
            end = min(v, N // q)
            for i in range(1, end + 1):
                d = i * p
                if d <= v:
                    larges[i] -= (larges[d] - p_sum) * p
                else:
                    larges[i] -= (smalls[N // d] - p_sum) * p
            for i in range(v, q - 1, -1):
                smalls[i] -= (smalls[i // p] - p_sum) * p
        return smalls, larges

    if N <= 5:
        return 0

    sqrt_N = isqrt(N)
    cbrt_N = icbrt(N)

    # about O(N^(3/4))
    psum_smalls, psum_larges = tabulate_all_primes_sum(N)

    primes = prime_sieve(sqrt_N)

    pis = [0] * (sqrt_N + 1)
    prime_power_sum_delta = [0] * (sqrt_N + 1)
    for p in primes:
        pis[p] = 1
        q = p
        p2 = p * p
        while q <= sqrt_N:
            prime_power_sum_delta[q] = q if q % p2 != 0 else q - q // p
            q *= p

    for i in range(1, sqrt_N + 1):
        pis[i] += pis[i - 1]

    ans = 0

    # sum { (p, q) | q * q > N }
    pwsum = 0
    for i in range(2, sqrt_N):
        pwsum += prime_power_sum_delta[i]
        ans += pwsum * (psum_larges[i] - psum_larges[i + 1])

    if sqrt_N != N // sqrt_N:
        pwsum += prime_power_sum_delta[sqrt_N]
        ans += pwsum * (psum_larges[sqrt_N] - psum_smalls[sqrt_N])

    # sum { (p, q) | q ** 3 > N, sqrt(N / q) < p < q }
    for pi in range(pis[sqrt_N], pis[cbrt_N], -1):
        q = primes[pi - 1]
        ans += q * (psum_smalls[q - 1] - psum_smalls[isqrt(N // q)])

    # sum { (p, q) | otherwise } ; about O(N^(3/4))
    for pi in range(pis[sqrt_N]):
        q = primes[pi]
        qmax = q
        while qmax * q <= N:
            qmax *= q

        for pj in range(min(pi, pis[isqrt(N // q)])):
            p = primes[pj]
            prod = qmax
            mx = 0
            while 1:
                while prod * p <= N:
                    prod *= p
                    mx = max(mx, prod)
                prod //= q
                if prod % q != 0:
                    break
            ans += mx
    return ans


from mylib import StopWatch

with StopWatch():
    print(prob347(10**7))
