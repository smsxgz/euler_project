def sum_divisors(n):
    phi = [0] * (n + 1)
    phi[1] = 1
    for i in range(2, n + 1):
        if not phi[i]:
            p = i
            mul = 1
            while p <= n:
                for j in range(p, n + 1, p):
                    if not phi[j]:
                        phi[j] = j
                    phi[j] = phi[j] // i // mul * (mul + p)
                mul += p
                p *= i
    for i in range(1, n + 1):
        phi[i] -= i
    return phi


def sum_divisors1(limit):
    dsums = [1] * (limit + 1)
    sq = int((limit + 0.5)**.5)
    for i in range(2, sq + 1):
        dsums[i * i] += i

        ulimit = limit // i
        if limit % i != 0:
            ulimit += 1
        for k in range(i + 1, ulimit):
            dsums[k * i] += (k + i)
    return dsums


def solve(N=10**6):
    s = sum_divisors(N)
    visited = set([1])

    longest_chain = 1
    res = None
    for i in range(2, N + 1):
        t = i
        amicable_chain = [i]
        while True:
            if t in visited:
                break
            visited.add(t)
            t = s[t]
            if t > N:
                break
            elif t in amicable_chain:
                length = len(amicable_chain) - amicable_chain.index(t)
                if longest_chain < length:
                    res = amicable_chain + [t]
                    longest_chain = length
                break
            else:
                amicable_chain.append(t)
    print(longest_chain, res)
    # return longest_chain, res


if __name__ == '__main__':
    from mylib import StopWatch
    with StopWatch():
        solve()
