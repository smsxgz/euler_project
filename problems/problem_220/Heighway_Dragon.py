def turn(x, y, d):
    if d == 0:
        return x, y
    elif d == 1:
        return -y, x
    elif d == 2:
        return -x, -y
    else:
        return y, -x


def step(k):
    res = dict()
    res[(0, 'a')] = 0, 0, 0
    res[(0, 'b')] = 0, 0, 0

    ax, ay, al = 0, 0, 0
    bx, by, bl = 0, 0, 0

    for i in range(1, k + 1):
        # aRbFR
        nax, nay, nal = ax, ay, al
        nal -= 1
        dx, dy = turn(bx, by, nal % 4)
        nax, nay = nax + dx, nay + dy
        nal += bl
        dx, dy = turn(0, 1, nal % 4)
        nax, nay = nax + dx, nay + dy
        nal -= 1
        nal %= 4

        # LFaLb
        nbx, nby, nbl = -1, 0, 1
        dx, dy = turn(ax, ay, nbl)
        nbx, nby = nbx + dx, nby + dy
        nbl += al + 1
        dx, dy = turn(bx, by, nbl % 4)
        nbx, nby = nbx + dx, nby + dy
        nbl += bl
        nbl %= 4

        ax, ay, al = nax, nay, nal
        bx, by, bl = nbx, nby, nbl

        res[(i, 'a')] = (ax, ay, al)
        res[(i, 'b')] = (bx, by, bl)
    return res


step = step(50)


def transform(x, y, d, k, flag):
    sx, sy, sl = step[(k, flag)]
    dx, dy = turn(sx, sy, d)
    d += sl
    return (x + dx, y + dy), d % 4


def solve(p, d, n, k, flag='a'):
    D = 2**(k - 1) - 1
    if flag == 'a':
        # aRbFR
        if n <= D:
            return solve(p, d, n, k - 1, flag='a')

        np, nd = transform(*p, d, k - 1, 'a')
        nd -= 1
        if n <= 2 * D:
            return solve(np, nd % 4, n - D, k - 1, flag='b')

        np, nd = transform(*np, nd % 4, k - 1, 'b')
        dx, dy = turn(0, 1, nd)
        return (np[0] + dx, np[1] + dy)

    if flag == 'b':
        # LFaLb
        nd = (d + 1) % 4
        dx, dy = turn(0, 1, nd)
        np = (p[0] + dx, p[1] + dy)
        if n == 1:
            return np

        if n <= D + 1:
            return solve(np, nd, n - 1, k - 1, flag='a')

        np, nd = transform(*np, nd, k - 1, 'a')
        nd += 1
        return solve(np, nd % 4, n - D - 1, k - 1, flag='b')


if __name__ == "__main__":
    print(solve((0, 1), 0, 499, 10))
    print(solve((0, 1), 0, 10**12-1, 50))
