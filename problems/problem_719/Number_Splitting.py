def split(goal, digits):
    if digits < goal:
        return False

    elif digits == goal:
        return True

    t = 10
    while t < digits:
        cutoff = digits // t
        rest = digits % t
        if rest < goal:
            if split(goal - rest, cutoff):
                return True
        else:
            break

        t *= 10

    return False


def main(N):
    res = 0
    for i in range(1, N + 1):
        if i % 9 != 0 and i % 9 != 1:
            continue

        sq = i * i
        if split(i, sq):
            res += sq
    print(res)


if __name__ == '__main__':
    main(100)
    main(10**6)
