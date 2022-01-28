def solve(p, q):
    path = []
    pre = None
    c = 0
    while q > 0:
        if p > q:
            if pre is None or pre == 0:
                c += 1
            else:
                path.append(c)
                c = 1

            pre = 0
            p -= q

        elif p <= q:
            if pre is None or pre == 1:
                c += 1
            else:
                path.append(c)
                c = 1

            pre = 1
            q -= p
    path.append(c)

    return path[::-1]


if __name__ == '__main__':
    print(solve(13, 17))
    print(solve(123456789, 987654321))
