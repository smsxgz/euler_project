import time
import math
import heapq


def solve(matrix, size):
    x, y = size
    sum_matrix = {}

    for i in range(x):
        sum_matrix[(i, 0)] = matrix[(i, 0)]

    for j in range(1, y):
        cumsum = [0]
        for i in range(x):
            cumsum.append(cumsum[-1] + matrix[(i, j)])
        for i in range(x):
            min_sum = sum_matrix[(i, j - 1)] + matrix[(i, j)]
            for ii in range(x):
                if i > ii:
                    min_sum = min(
                        sum_matrix[(ii, j - 1)] + cumsum[i + 1] - cumsum[ii],
                        min_sum)
                else:
                    min_sum = min(
                        sum_matrix[(ii, j - 1)] + cumsum[ii + 1] - cumsum[i],
                        min_sum)
            sum_matrix[(i, j)] = min_sum

    return min(sum_matrix[(i, y - 1)] for i in range(x))


def main():
    matrix = {}
    with open('matrix.txt', 'r') as f:
        for i, line in enumerate(f.readlines()):
            for j, s in enumerate(line.strip().split(',')):
                matrix[(i, j)] = int(s)
    r, c = sorted(matrix.keys(), key=lambda x: sum(x))[-1]

    start = time.time()
    print(solve(matrix, (r + 1, c + 1)))
    print(time.time() - start)


class Graph(dict):
    def get_neiborhood(self, pos, size):
        i, j = pos
        x, y = size

        if pos == (0, -1):
            for ix in range(x):
                yield (ix, 0), self.get((ix, 0))
        else:
            if j == y - 1:
                yield (0, y), 0

            for dx, dy in ((1, 0), (0, 1), (-1, 0)):
                v = self.get((i + dx, j + dy))
                if v:
                    yield (i + dx, j + dy), v


def dijkstra(graph, size):
    x, y = size
    start = (0, -1)
    target = (0, y)
    dest = None

    visited = set()
    dist_matrix = {start: 0}

    heap = [(0, start)]
    heapq.heapify(heap)

    while heap and dest is None:
        cur_dist, current = heapq.heappop(heap)
        visited.add(current)

        for next_vertex, value in graph.get_neiborhood(current, size):
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


def main1():
    matrix = Graph()
    with open('matrix.txt', 'r') as f:
        for i, line in enumerate(f.readlines()):
            for j, s in enumerate(line.strip().split(',')):
                matrix[(i, j)] = int(s)
    r, c = sorted(matrix.keys(), key=lambda x: sum(x))[-1]

    start = time.time()
    print(dijkstra(matrix, (r + 1, c + 1)))
    print(time.time() - start)


def leastCost(matrix, size):
    costs = {}
    x, y = size

    for i in range(x):
        costs[(i, y - 1)] = matrix[(i, y - 1)]

    for j in range(y - 2, -1, -1):
        for i in range(x):
            value = matrix[(i, j)]
            costs[(i, j)] = value + costs[(i, j + 1)]
            costs[(i, j)] = min(costs[(i, j)], value + costs.get(
                (i - 1, j), math.inf))
        for i in range(x - 1, -1, -1):
            costs[(i, j)] = min(costs[(i, j)], matrix[(i, j)] + costs.get(
                (i + 1, j), math.inf))

    return min(costs[(i, 0)] for i in range(x))


def main2():
    matrix = {}
    with open('matrix.txt', 'r') as f:
        for i, line in enumerate(f.readlines()):
            for j, s in enumerate(line.strip().split(',')):
                matrix[(i, j)] = int(s)
    r, c = sorted(matrix.keys(), key=lambda x: sum(x))[-1]

    start = time.time()
    print(leastCost(matrix, (r + 1, c + 1)))
    print(time.time() - start)


if __name__ == '__main__':
    main()
    main1()
    main2()
