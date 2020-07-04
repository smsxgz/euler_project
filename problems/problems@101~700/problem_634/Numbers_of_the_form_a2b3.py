import time


class StopWatch:
    def __enter__(self, *args):
        self.start = time.time()

    def __exit__(self, *args):
        print(time.time() - self.start)


def powrt(n, pow=2):
    return int((n + 0.5)**(1 / pow))


def euler_prime(n):
    prime = []
    vis = [0] * (n + 1)
    for i in range(2, n + 1):
        if not vis[i]:
            prime.append(i)
        for p in prime:
            if i * p > n:
                break
            vis[i * p] = 1
            if (i % p == 0):
                break
    return prime


def Mobius(n):
    prime = [1] * (n + 1)
    mobius = [1] * (n + 1)

    for i in range(2, n + 1):
        if not prime[i]:
            continue
        mobius[i] = -1
        for j in range(2, n // i + 1):
            prime[i * j] = 0
            mobius[i * j] *= -1
        for j in range(1, n // (i * i) + 1):
            mobius[j * i * i] = 0
    return mobius


def square_free(mobius, n):
    s = 0
    for i in range(1, powrt(n) + 1):
        s += mobius[i] * (n // (i * i))
    return s


def cube_free(mobius, n):
    s = 0
    for i in range(1, powrt(n, 3) + 1):
        s += mobius[i] * (n // (i * i * i))
    return s


def solve(N):
    cb = powrt(N // 4, 3)
    mobius = Mobius(cb)

    s = 0
    for i in range(2, cb + 1):
        if mobius[i]:
            s += cube_free(mobius, powrt(N // (i * i * i))) - 1

    rt6 = powrt(N, 6)
    for t in range(2, rt6 + 1):
        n = N // (t**6)
        for i in range(1, powrt(n + 1, 3) + 1):
            if mobius[i]:
                s += cube_free(mobius, powrt(n // (i * i * i)))
        s -= 1

    s += rt6 - 1 - len(euler_prime(rt6))

    return s


def solve2(N):
    cb = powrt(N // 4, 3)
    mobius = Mobius(cb)
    s = 0
    for b in range(2, cb + 1):
        s += abs(mobius[b]) * (powrt(N // (b**3)) - 1)

    s += powrt(N) - cube_free(mobius, powrt(N)) - len(euler_prime(powrt(N, 6)))
    return s


def solve3(N):
    pass


if __name__ == '__main__':
    N = int(float(input()))
    with StopWatch():
        print(solve(N))

    with StopWatch():
        print(solve2(N))
