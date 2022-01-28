seq = []
for k in range(1, 56):
    seq.append((100003 - 200003 * k + 300007 * k**3) % 1000000 - 500000)

for k in range(56, 4000001):
    seq.append((seq[-24] + seq[-55] + 1000000) % 1000000 - 500000)

matrix = []
for i in range(2000):
    matrix.append(seq[i * 2000:(i + 1) * 2000])


def greatest_sum(lst):
    current_greatest = greatest = lst[0]
    for n in lst[1:]:
        if current_greatest > 0:
            current_greatest = n + current_greatest
        else:
            current_greatest = n
        greatest = max(greatest, current_greatest)
    return greatest


res = 0
# horizontal
for i in range(2000):
    res = max(res, greatest_sum(matrix[i]))

# vertical
for j in range(2000):
    res = max(res, greatest_sum([matrix[i][j] for i in range(2000)]))

# diagonal
for j in range(2000):
    res = max(res, greatest_sum([matrix[i][j + i] for i in range(2000 - j)]))
for i in range(1, 2000):
    res = max(res, greatest_sum([matrix[i + j][j] for j in range(2000 - i)]))

# anti-diagonal
for j in range(2000):
    res = max(res, greatest_sum([matrix[i][j - i] for i in range(j + 1)]))
for i in range(1, 2000):
    res = max(res,
              greatest_sum([matrix[i + j][1999 - j] for j in range(2000 - i)]))

print(res)
