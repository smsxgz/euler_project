from collections import defaultdict

N = 30

cache = defaultdict(dict)
cache[2]['OA'] = 1
cache[2]['AA'] = 1
cache[2]['OO'] = 1
cache[2]['AO'] = 1

for i in range(3, N + 1):
    cache[i]['OA'] = cache[i - 1]['AO'] + cache[i - 1]['OO']
    cache[i]['AA'] = cache[i - 1]['OA']
    cache[i]['OO'] = cache[i - 1]['AO'] + cache[i - 1]['OO']
    cache[i]['AO'] = cache[i - 1]['AA'] + cache[i - 1]['OA']

res = dict()
res[0] = 1
res[1] = 2
for i in range(2, N + 1):
    res[i] = sum(cache[i].values())

e = res[N]
for i in range(1, N + 1):
    e += res[i - 1] * res[N - i]
print(e)
