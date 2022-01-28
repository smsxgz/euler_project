def Transition(pat):
    # Let lps[i][j] be the longest suffix of pat[:i] + [j]
    # which is also a prefix of pat
    M = len(pat)
    lps = [[0 for _ in range(10)] for _ in range(M)]

    lps[0][int(pat[0])] = 1

    for i in range(1, M):
        for j in range(10):
            tmp = pat[:i] + str(j)
            for k in range(i + 1, -1, -1):
                if tmp[-k:] == pat[:k]:
                    lps[i][j] = k
                    break

    trans = [[0 for _ in range(M + 1)] for _ in range(M)]
    for i in range(M):
        for j in lps[i]:
            trans[i][j] += 1

    return trans


def solve(trans):
    M = len(trans)
    for i in range(M):
        trans[i][i] -= 10

    s = [0] * (M + 1)
    for i in range(M):
        s[i + 1] -= 10
        for j in range(i + 1):
            s[i + 1] -= trans[i][j] * s[j]
    # print(s)
    return 1 - s[-1] - M


def main():
    N = 10**16

    res = 0
    for n in range(2, 10**6):
        if n % 10000 == 0:
            print(n)
        pat = str(N // n)
        trans = Transition(pat)
        res += solve(trans)
    print(res)


if __name__ == "__main__":
    main()
