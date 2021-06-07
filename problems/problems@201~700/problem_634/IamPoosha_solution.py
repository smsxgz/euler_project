import math
import time


class StopWatch:
    def __enter__(self, *args):
        self.start = time.time()

    def __exit__(self, *args):
        print(time.time() - self.start)


# int(x ^ (1/n))
def integer_root(x, n):
    # maybe need to add the -1 for pathalogical cases.
    if n == 2:
        res = int(math.sqrt(x))  # - 1
        while (res + 1) * (res + 1) <= x:
            res += 1
    else:
        res = int(x**(1. / n))  # - 1
        while (res + 1)**n <= x:
            res += 1
    return res


def recursive_compute_stuff(init_sieve, init_val, nxt_idx, idx_comp):
    if not init_sieve:
        init_sieve = [0]
    cache = dict()

    def calc(n):
        if n < len(init_sieve):
            return init_sieve[n]
        if n in cache:
            return cache[n]
        res = init_val(n)
        idx = 2
        try:
            while 1:
                idx, prv = nxt_idx(n, idx), idx
                # for more generality, can have here coefficient.
                res -= (idx - prv) * calc(idx_comp(n, prv))
        except Exception:
            cache[n] = res
            return res

    return calc


def primes_upto(n):
    sieve = [True] * ((n + 1) // 2)
    for i in range(3, integer_root(n, 2) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2::i] = [False] * ((n - i * i) // (2 * i) + 1)
    return sum(sieve) - (n < 2)


def sf_sieve(n):
    res = [1] * (n + 1)
    res[0] = 0
    for p in range(2, n):
        pp = p * p
        if pp > n:
            break
        if res[pp]:
            res[pp:n + 1:pp] = [0] * (n // pp)
    for i in range(1, len(res)):
        res[i] += res[i - 1]
    return res


def cf_sieve(n):
    res = [1] * (n + 1)
    res[0] = 0
    for p in range(2, n):
        pp = p * p * p
        if pp > n:
            break
        if res[pp]:
            res[pp:n + 1:pp] = [0] * (n // pp)
    for i in range(1, len(res)):
        res[i] += res[i - 1]
    return res


def F(n):
    ir2 = integer_root(n, 2)
    ir213 = integer_root(n**2, 13)
    ir313 = integer_root(n // ir213**2, 3)
    # some constants resulting from different efficiencies
    # and lower order factors.
    csf = sf_sieve(5 * ir313)
    square_free_upto = recursive_compute_stuff(
        csf, lambda tt: tt,
        lambda tt, ii: integer_root(tt // (tt // (ii * ii)), 2) + 1,
        lambda tt, ii: tt // (ii * ii))
    cubic_free_upto = recursive_compute_stuff(
        cf_sieve(int(30 * n**(2. / 13))), lambda tt: tt,
        lambda tt, ii: integer_root(tt // (tt // (ii * ii * ii)), 3) + 1,
        lambda tt, ii: tt // (ii * ii * ii))
    # computable in n**(3/13)
    res = 0
    for rr in range(1, ir213):
        res += rr * (square_free_upto(integer_root(n // rr**2, 3)) -
                     square_free_upto(integer_root(n // (rr + 1)**2, 3)))
    for x in range(2, ir313 + 1):
        if csf[x] > csf[x - 1]:
            res += integer_root(n // x**3, 2)
    # need to add the *set* of the numbers expressible in the form
    #    a^2 * t^6,   1 not in {a,t},  a -- cubic free.
    #    b^3 * t^6,   1 not in {b,t},  b -- square free.
    res += ir2
    res -= primes_upto(integer_root(n, 6)) + 1
    res -= cubic_free_upto(ir2) - 1
    res -= square_free_upto(integer_root(n, 3)) - 1
    return res


if __name__ == '__main__':
    with StopWatch():
        print("solution:", F(9 * 10**18))
    # print("sport:", F(15 * 10**30))
