class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent

    def __str__(self):
        s = [str(self.value)]
        node = self.parent
        while node:
            s.append(str(node.value))
            node = node.parent
        return '<-'.join(s)


def expand_leaves(node):
    v = node.value
    n = node
    while node:
        yield Node(v + node.value, n)
        node = node.parent


def BFS(n):
    res = [0] * (n + 1)
    nodes = [Node(1)]
    depth = 1

    while not all(res[2:]):
        leaves = []
        for node in nodes:
            for leaf in expand_leaves(node):
                leaves.append(leaf)
                if leaf.value <= n and not res[leaf.value]:
                    res[leaf.value] = depth
                    # print(str(leaf))
        nodes = leaves
        depth += 1

    return res


if __name__ == "__main__":
    r = BFS(200)
    # print(str(r[127]))
    print(sum(r))
