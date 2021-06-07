import random


#################################################
# For max-matching
def DFS_hungarian(matrix):
    n = len(matrix)
    ans = 0
    matching = dict((i, -1) for i in range(2 * n))

    def DFS(v):
        line = matrix[v]
        for u in range(n, 2 * n):
            if line[u - n] == 1 and check[u] == 0:
                check[u] = 1
                if matching[u] == -1 or DFS(matching[u]):
                    matching[u] = v
                    matching[v] = u
                    return True
        return False

    for v in range(n):
        if matching[v] == -1:
            check = dict((j, 0) for j in range(2 * n))
            if DFS(v):
                ans += 1

    return ans


def BFS_hungarian(matrix):
    n = len(matrix)
    ans = 0
    Q = []
    matching = dict((i, -1) for i in range(2 * n))
    check = dict((i, -1) for i in range(2 * n))
    prev = dict((i, -1) for i in range(2 * n))

    def update_matching(d, e):
        while d != -1:
            t = matching[d]
            matching[d] = e
            matching[e] = d
            d = prev[d]
            e = t

    for v in range(n):
        if matching[v] == -1:
            Q.clear()
            Q.append(v)
            prev[v] = -1  # set v as beginner of the path
            flag = False
            while len(Q) > 0 and not flag:
                u = Q.pop(0)
                line = matrix[u]
                for w in range(n, 2 * n):
                    if line[w - n] == 1 and check[w] != v:
                        check[w] = v
                        Q.append(matching[w])
                        if matching[w] >= 0:
                            prev[matching[w]] = u
                        else:
                            flag = True
                            update_matching(u, w)
                            break

            if matching[v] != -1:
                ans += 1

    return ans


n = 100
matrix = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        if random.random() > 0.99:
            matrix[i][j] = 1

DFS_hungarian(matrix)
BFS_hungarian(matrix)
