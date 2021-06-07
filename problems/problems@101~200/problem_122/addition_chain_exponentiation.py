MAX = 200
nmult = [0] + ([MAX] * MAX)
node = [0] * 16  # 2*log2(MAX) rounded up


def build_tree(e=1, n=0):
    if e > MAX or n > nmult[e]:
        return
    node[n], nmult[e] = e, n
    for i in range(n, -1, -1):
        build_tree(node[i] + e, n + 1)


build_tree()
print(sum(nmult))
