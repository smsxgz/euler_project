# -*- coding: utf-8 -*-
with open('p042_words.txt') as f:
    words = f.readline().strip().replace('"', '').split(',')


def triangle_generator():
    i = 1
    t = 1
    while True:
        yield t
        i += 1
        t += i


w = 'qwertyuiopasdfghjklzxcvbnm'
w = sorted(w)
d = {}
for i, letter in enumerate(w):
    d[letter] = i + 1

g = triangle_generator()
t = next(g)
t_max = t
t_set = {t}
m = 0
for word in words:
    score = sum([d[letter] for letter in word.lower()])
    while score > t_max:
        t = next(g)
        t_max = t
        t_set.add(t)
    if score in t_set:
        m += 1
print(m)
