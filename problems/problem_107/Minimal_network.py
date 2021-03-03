import heapq

with open('p107_network.txt', 'r') as f:
    matrix = f.readlines()

N = len(matrix)
h = []
idx = 0
nodes = set()
edge_wights = 0
nodes.add(idx)
while len(nodes) < N:
    for j, w in enumerate(matrix[idx].strip().split(',')):
        if w != '-' and j not in nodes:
            wight = int(w)
            heapq.heappush(h, (wight, (idx, j)))
    while True:
        wight, edge = heapq.heappop(h)
        if edge[1] not in nodes:
            edge_wights += wight
            idx = edge[1]
            nodes.add(idx)
            break
print(edge_wights)

res = 0
for line in matrix:
    line = line.strip().split(',')
    for w in line:
        if w != '-':
            res += int(w)
print(res // 2 - edge_wights)
