# -*- coding: utf-8 -*-
import time


def Coin_sums(n):
    l = [1, 2, 5, 10, 20, 50, 100, 200]
    c = [[1, 1, 1, 1, 1, 1, 1, 1]]
    for i in range(1, n + 1):
        cc = [1]
        for j in range(1, 8):
            if i >= l[j]:
                cc.append(cc[-1] + c[i - l[j]][j])
            else:
                cc.append(cc[-1])
        c.append(cc)
    return cc[-1]


def Coin_sums1(n):
    l = [1, 2, 5, 10, 20, 50, 100, 200]
    c = [1] * 201
    for i in range(1, 8):
        ll = l[i]
        for j in range(ll, 201):
            c[j] += c[j - ll]
    return c[-1]


class stopwatch():
    def __enter__(self):
        self.start = time.time()

    def __exit__(self, unused_exception_type, unused_exc_value,
                 unused_traceback):
        print(time.time() - self.start)


with stopwatch():
    print(Coin_sums(200))

with stopwatch():
    print(Coin_sums1(200))
