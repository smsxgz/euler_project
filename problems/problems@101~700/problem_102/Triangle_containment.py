import numpy as np


class Triangle(object):
    def __init__(self, l):
        self.tri = np.array(l).reshape(3, 2)

    @property
    def origin_contain(self):
        tri_s = self.tri[[1, 2, 0]][:, [1, 0]]
        tri_s[:, 0] = -tri_s[:, 0]
        a = np.sum(tri_s * self.tri, axis=1)
        return (a > 0).all() or (a < 0).all()


tot = 0
f = open('p102_triangles.txt', 'r')
for line in f.readlines():
    l = [int(s) for s in line.strip().split(',')]
    t = Triangle(l)
    if t.origin_contain:
        tot += 1
print(tot)
