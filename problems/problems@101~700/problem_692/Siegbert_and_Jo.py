def main(N):
    fibo1, fibo2 = 1, 1
    g1, g2 = 1, 1
    # ssum = 1

    while True:
        fibo1, fibo2 = fibo2, fibo1 + fibo2
        if fibo2 > N:
            break
        g1, g2 = g2, g1 + g2 + fibo1

    return g2


def main2(N):
    ssum = 1
    fibo1 = 1
    fibo2 = 1

    min_win = [0, 1]

    while True:
        for i in range(fibo2 + 1, fibo1 + fibo2 + 1):
            if i > N:
                return ssum
            if i < fibo1 + fibo2:
                mv = min_win[i - fibo2]
            else:
                mv = i
            min_win.append(mv)
            ssum += mv
        fibo1, fibo2 = fibo2, fibo1 + fibo2


if __name__ == '__main__':
    print(main(13))
    print(main(23416728348467685))
