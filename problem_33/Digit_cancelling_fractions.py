# -*- coding: utf-8 -*-
for a in range(1, 10):
    for b in range(1, 10):
        m = 10 * a * b
        n = 9 * a + b
        if m % n == 0:
            c = m // n
            if a != c:
                print(a, b, c)
