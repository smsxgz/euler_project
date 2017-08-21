# -*- coding: utf-8 -*-
import itertools
import time


class stopwatch():
    def __enter__(self):
        self.start = time.time()

    def __exit__(self, unused_exception_type, unused_exc_value,
                 unused_traceback):
        print(time.time() - self.start)


# Stupid methed !!!
with stopwatch():
    s = list(range(1, 1000))
    d = {}

    l = [1, 9]
    while True:
        for idx, n in enumerate(l):
            for i in s:
                if i > n:
                    break
                if n % i == 0:
                    s.remove(i)
                    d[i] = idx
        l = [n * 10 for n in l]
        l.append(l[-1] + 9)
        if len(s) == 0:
            break

    max(d, key=lambda x: d[x])


def reciprocal_cycle_len(n):
    seen = {}
    x = 1
    for i in itertools.count():
        if x in seen:
            return i - seen[x]
        else:
            seen[x] = i
            x = x * 10 % n


with stopwatch():
    ans = max(range(1, 1000), key=reciprocal_cycle_len)
