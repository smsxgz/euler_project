from collections import defaultdict
from mylib import sqrt


def is_square(n):
    sq = sqrt(n)
    return sq * sq == n


def match(word, square):
    assign = dict()
    used = set()
    for ch, ss in zip(word, str(square)):
        if ch in assign:
            if assign[ch] != ss:
                return False
        else:
            if ss in used:
                return False
            else:
                assign[ch] = ss
                used.add(ss)
    res = ''
    for ch in sorted(assign.keys()):
        res += f'{ch}{assign[ch]}'
    return res


def assignments(words, squares):
    for word in words:
        for sq in squares:
            assign = match(word, sq)
            if assign:
                yield assign
    return


def main():
    with open('p098_words.txt', 'r') as f:
        words = f.readline().split(',')
        words = [w[1:-1] for w in words]

    anagrams = defaultdict(list)

    for w in words:
        key = "".join(sorted(w))
        anagrams[key].append(w)

    keys = sorted(anagrams.keys(), key=lambda x: -len(x))

    res = 0
    length = 99
    for key in keys:
        if len(anagrams[key]) <= 1:
            continue

        if len(key) < length:
            if res:
                print(res)
                return res
            else:
                length = len(key)
                lo = sqrt(10**(length - 1))
                up = sqrt(10**(length))
                squares = [i * i for i in range(lo + 1, up + 1)]

        words = anagrams[key]

        tmp = defaultdict(dict)
        for word in words:
            for sq in squares:
                assign = match(word, sq)
                if assign:
                    tmp[word][assign] = sq

        for i in range(len(words)):
            w1 = words[i]
            for j in range(i + 1, len(words)):
                w2 = words[j]
                a = list(tmp[w1].keys() & tmp[w2].keys())
                if len(a) >= 1:
                    res = max(res, tmp[w1][a[0]], tmp[w2][a[0]])


if __name__ == '__main__':
    main()
