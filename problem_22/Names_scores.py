# -*- coding: utf-8 -*-
s = 'qwertyuiopasdfghjklzxcvbnm'
s = sorted(s)
d = {}
for i, letter in enumerate(s):
    d[letter] = i + 1


def nameworth(name):
    worth = 0
    for letter in name:
        worth += d[letter]
    return worth


with open('p022_names.txt', 'r') as f:
    data = f.readline().strip().replace('"', '').split(',')

data.sort()
scores = 0
for i, name in enumerate(data):
    scores += (i + 1) * nameworth(name.lower())
scores
