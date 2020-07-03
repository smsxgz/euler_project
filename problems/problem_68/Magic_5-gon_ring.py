def search(total, solution=[], unused=set(range(1, 11))):
    if len(solution) == 0:
        for s1 in range(1, 7):
            unused.remove(s1)
            for s2 in list(unused):
                s3 = total - s1 - s2
                if s2 != s3 and s3 in unused:
                    unused.remove(s2)
                    unused.remove(s3)
                    yield from search(total, solution + [(s1, s2, s3)], unused)
                    unused.add(s3)
                    unused.add(s2)
            unused.add(s1)
        return

    elif len(solution) == 4:
        assert len(unused) == 1

        s = list(unused)[0]
        if s + solution[0][1] + solution[-1][2] == total:
            yield solution + [(s, solution[-1][2], solution[0][1])]
            return

    else:
        for s1 in list(unused):
            if s1 < solution[0][0]:
                continue
            s2 = total - s1 - solution[-1][2]
            if s1 != s2 and s2 in unused:
                unused.remove(s1)
                unused.remove(s2)
                yield from search(total,
                                  solution + [(s1, solution[-1][2], s2)],
                                  unused)
                unused.add(s1)
                unused.add(s2)
        return


def main():
    res = -1
    for total in range(14, 20):
        for solution in search(total):
            tmp = ''
            for tp in solution:
                tmp += '{}{}{}'.format(*tp)
            if len(tmp) == 16:
                res = max(res, int(tmp))
    print(res)


if __name__ == '__main__':
    main()
