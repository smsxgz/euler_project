mem = {(0, ''): True}


def split(goal, n_str):
    if (goal, n_str) in mem:
        return mem[(goal, n_str)]

    for i in range(1, len(n_str) + 1):
        if int(n_str[:i]) <= goal:
            if split(goal - int(n_str[:i]), n_str[i:]):
                mem[(goal, n_str)] = True
                return True
        else:
            break
    mem[(goal, n_str)] = False
    return False


def main(N):
    res = 0
    for i in range(1, N + 1):
        if i % 10000 == 0:
            print(i)
        sq = i * i
        if split(i, str(sq)):
            res += sq
    print(res)


if __name__ == '__main__':
    main(100)
    main(10**6)
