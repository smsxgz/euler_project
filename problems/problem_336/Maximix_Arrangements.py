def arrangments():
    res = []
    cache = [('ABCDEFGHIKJ', 3)]
    while cache:
        s, i = cache.pop(0)
        n = len(s)
        s = s[:n - i] + s[-i:][::-1]
        for j in range(2, i):
            t = s[:n - j] + s[-j:][::-1]
            if i == n:
                res.append(t)
            else:
                cache.append((t, i + 1))
    res.sort()
    return res


if __name__ == "__main__":
    r = arrangments()
    print(r[2010])
