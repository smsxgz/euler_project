prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]


def prod(lst):
    res = 1
    for p in lst:
        res *= p
    return res


class Solution:
    def __init__(self, N=8000000):
        self.N = N

        q = 3
        e = 1
        while q < self.N:
            q *= 3
            e += 1

        self.base_product = prod(prime[:e])
        self.mem = set()

        for i in range(e - 1, 0, -1):
            base_lst = [3] * i
            self.find_min_product(base_lst, prod(prime[:i]), 3**i)

        print(self.base_product)

    def find_min_product(self, lst, product, factors):

        if factors > self.N:
            if product < self.base_product:
                self.base_product = product
            return

        for i in range(len(lst)):
            if i == 0 or lst[i - 1] > lst[i]:
                tl = lst.copy()
                tl[i] += 2
                # print(tl, product, self.base_product)
                key = tuple(tl)
                if key not in self.mem:
                    self.mem.add(key)

                    tp = product * prime[i]
                    tf = factors // lst[i] * (lst[i] + 2)
                    if tp > self.base_product:
                        continue
                    self.find_min_product(tl, tp, tf)

        return


if __name__ == '__main__':
    Solution(2000)
    Solution(8000000)
