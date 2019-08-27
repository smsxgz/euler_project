import math
import heapq


class Graph(dict):
    def get_neiborhood(self, pos):
        i, j = pos
        for dx, dy in ((1, 0), (0, 1), (0, -1), (-1, 0)):
            v = self.get((i + dx, j + dy))
            if v:
                yield (i + dx, j + dy), v


def dijkstra(graph, size):
    x, y = size
    start = (0, 0)
    target = (x - 1, y - 1)
    dest = None

    visited = set()
    dist_matrix = {start: graph[start]}

    heap = [(graph[start], start)]
    heapq.heapify(heap)

    while len(visited) < x * y and dest is None:
        cur_dist, current = heapq.heappop(heap)
        visited.add(current)

        for next_vertex, value in graph.get_neiborhood(current):
            if next_vertex in visited:
                continue
            new_dist = cur_dist + value

            if new_dist < dist_matrix.get(next_vertex, math.inf):
                dist_matrix[next_vertex] = new_dist
                heapq.heappush(heap, (new_dist, next_vertex))
            if next_vertex == target:
                dest = new_dist
                break
    return dest


import time


def main():
    matrix = Graph()
    with open('matrix.txt', 'r') as f:
        for i, line in enumerate(f.readlines()):
            for j, s in enumerate(line.strip().split(',')):
                matrix[(i, j)] = int(s)
    r, c = sorted(matrix.keys(), key=lambda x: sum(x))[-1]

    start = time.time()
    print(dijkstra(matrix, (r + 1, c + 1)))
    print(time.time() - start)


def q83():
    with open('matrix.txt', 'r') as f:
        grid = [[int(y) for y in x.split(',')]
                for x in [x.rstrip() for x in f.readlines()]]

    start = time.time()
    paths = [[math.inf for x in range(82)] for y in range(82)]
    paths[1][0] = 0
    for i in range(0, 4):
        for j in range(1, 81):
            for k in range(1, 81):
                paths[k][j] = min([
                    paths[k + 1][j], paths[k - 1][j], paths[k][j + 1],
                    paths[k][j - 1]
                ]) + grid[k - 1][j - 1]
    print(paths[80][80])
    print(time.time() - start)


if __name__ == '__main__':
    main()
    q83()
    # testMat = [[131, 673, 234, 103, 18], [201, 96, 342, 965, 150],
    #            [630, 803, 746, 422, 111], [537, 699, 497, 121,
    #                                        956], [805, 732, 524, 37, 331]]
    # mat = Graph()
    # for i, l in enumerate(testMat):
    #     for j, m in enumerate(l):
    #         mat[(i, j)] = m
    #
    # s = dijkstra(mat, (5, 5))
    # print(s)
    # def pprint(grid):
    #     for i in range(5):
    #         print(','.join([str(grid[(i, j)]) for j in range(5)]))
    #
    # pprint(s)
    # pprint(mat)
