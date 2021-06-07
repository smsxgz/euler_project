# from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot

        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def KruskalMST(self):
        self.graph = sorted(self.graph, key=lambda item: item[2])

        result = []
        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        i = 0
        e = 0
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        minimumCost = 0
        for u, v, weight in result:
            minimumCost += weight
            # print("%d -- %d == %d" % (u, v, weight))
        print("Minimum Spanning Tree", minimumCost)


if __name__ == "__main__":
    g = Graph(40)
    with open('p107_network.txt', 'r') as f:
        for i, line in enumerate(f.readlines()):
            line = line.strip().split(',')
            for j, w in enumerate(line[i + 1:], i + 1):
                if w != '-':
                    g.addEdge(i, j, int(w))

    g.KruskalMST()
