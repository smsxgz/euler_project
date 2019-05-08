from mylib import euler_prime, sqrt, StopWatch

prime = euler_prime(10000)


def is_prime(n):
    if n < 10000:
        return n in prime

    sq = sqrt(n)
    for p in prime:
        if p > sq:
            return True
        if n % p == 0:
            return False


num = len(prime)
cache = dict()

for i in range(1, num):
    p1 = prime[i]
    cache[p1] = set()
    for j in range(i + 1, num):
        p2 = prime[j]
        n1 = 10**len(str(p1)) * p2 + p1
        if is_prime(n1):
            n2 = 10**len(str(p2)) * p1 + p2
            if is_prime(n2):
                cache[p1].add(p2)


def longest_path(p, candidate=None):
    if candidate is None:
        candidate = cache[p]

    tmp = 0
    path = []
    for q in candidate:
        tmp_path = longest_path(q, candidate & cache[q])
        if len(tmp_path) > tmp:
            tmp = len(tmp_path)
            path = tmp_path

    return [p] + path


with StopWatch():
    for p in prime[1:]:
        path = longest_path(p)
        if len(path) == 5:
            print(path)
            print(sum(path))
