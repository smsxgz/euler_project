def is_palindromic(n):
    s = str(n)
    return s[::-1] == s


n = 10000
N = 10**8

# n = 32
# N = 1000

cache = dict()
cache[(1, 1)] = 1
res = set()
for i in range(2, n):
    s = i * i
    cache[(i, i)] = s

    for j in range(i - 1, 0, -1):
        cache[(j, i)] = cache[(j, i - 1)] + s
        if cache[(j, i)] > N:
            break
        if is_palindromic(cache[(j, i)]):
            res.add(cache[(j, i)])

print(sum(res))
# print(cache)
# print(cache[(6, 12)])
