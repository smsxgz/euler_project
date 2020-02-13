import gmpy2 as math
math.get_context().precision = 200


def solve(n):
    m = math.log(2)
    lo = math.log(1.23) / m
    hi = math.log(1.24) / m
    m = m / math.log(10)

    count = 0
    M = 0
    while count < n:
        M += 1
        if math.floor(lo + M / m) != math.floor(hi + M / m):
            count += 1

    return math.floor(hi + M / m)


if __name__ == "__main__":
    print(solve(45))
    print(solve(678910))
