M = 2**20
seq = [0]
for k in range(1, 500501):
    seq.append((615949 * seq[-1] + 797807) % M)
M >>= 1
seq = [n - M for n in seq]

matrix = []
for i in range(1, 1001):
    matrix.append(seq[i * (i - 1) // 2 + 1:i * (i + 1) // 2 + 1])

subtriangle = dict()
for d in range(1, 1001):
    for i in range(1001 - d):
        for j in range(i + 1):
            subtriangle[(i, j, d)] = matrix[i][j] + subtriangle.get(
                (i + 1, j, d - 1), 0) + subtriangle.get(
                    (i + 1, j + 1, d - 1), 0) - subtriangle.get(
                        (i + 2, j + 1, d - 2), 0)

print(min(subtriangle.values()))
