# -*- coding: utf-8 -*-
year = 1900
d = 1
s = 0
M = [[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
     [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]]
# 1 Jan 1901 to 31 Dec 2000
while True:
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        leap = 1
    else:
        leap = 0

    for days in M[leap]:
        d = (d + days) % 7
        if year > 1900 and d == 0:
            s += 1
    year += 1
    if year == 2001:
        break

s - (d == 0)
