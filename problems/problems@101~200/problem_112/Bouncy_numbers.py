def non_bouncy(prefix):
    b, flag = is_bouncy(prefix)
    if b:
        return 0
    s = prefix % 10
    x = (10 - s) * (11 - s) // 2
    y = (s + 1) * (s + 2) // 2
    if flag == 1:
        return x
    elif flag == -1:
        return y
    else:
        return x + y - 1


def is_bouncy(num):
    num = str(num)
    flag = 0
    s = int(num[0])

    for ch in num:
        if int(ch) > s:
            if flag == 0:
                flag = 1
            elif flag == -1:
                return True, flag
        elif int(ch) < s:
            if flag == 0:
                flag = -1
            elif flag == 1:
                return True, flag
        s = int(ch)
    return False, flag


def main():
    b = 99
    m = 1
    while True:
        b += non_bouncy(m)
        m += 1

        if b == m:
            print(100 * m)
            break


if __name__ == '__main__':
    from mylib import StopWatch
    with StopWatch():
        main()
