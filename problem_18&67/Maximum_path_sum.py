# -*- coding: utf-8 -*-
def Maximum_path_sum(triangle):
    s = [int(triangle.readline().strip())]
    print(s)
    l = 1
    for t in triangle.readlines():
        l += 1
        ss = []
        for i, n in enumerate(t.strip().split(' ')):
            if i == 0:
                ss.append(s[i] + int(n))
            elif i == l - 1:
                ss.append(s[i - 1] + int(n))
            else:
                ss.append(max(s[i], s[i - 1]) + int(n))
        s = ss
        print(s)
    return max(s)


with open('triangle.txt', 'r') as f:
    print(Maximum_path_sum(f))

with open('p067_triangle.txt', 'r') as f:
    print(Maximum_path_sum(f))
