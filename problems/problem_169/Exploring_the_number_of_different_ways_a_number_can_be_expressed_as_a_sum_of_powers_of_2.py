mem = dict()
mem[0] = 1
mem[1] = 1


def solve(n):
    if n in mem:
        return mem[n]

    m = n // 2
    if n % 2 == 0:
        r = solve(m - 1) + solve(m)
    else:
        r = solve(m)

    mem[n] = r
    return r


if __name__ == "__main__":
    print(solve(10**25))
