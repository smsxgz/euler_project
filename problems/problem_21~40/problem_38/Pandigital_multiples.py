import time


def is_zero(num):
    if '0' in list(str(num)):
        return True
    else:
        return False


def is_same(num):
    num_chr_list = list(str(num))
    for chr in list(str(num)):
        num_chr_list.remove(chr)
        if chr in num_chr_list:
            return False
    return True


def is_pandigital(x):
    str_pandigital = str(x)
    n = 2
    while True:
        str_pandigital += str(x * n)
        if is_zero(str_pandigital):
            return False
        if len(str_pandigital) == 9:
            if is_same(str_pandigital):
                return int(str_pandigital)
            else:
                return False
        if len(str_pandigital) > 9:
            return False
        n += 1


def main(is_pandigital):
    start_time = time.time()
    for i in range(9876, 1, -1):
        if is_pandigital(i):
            print(max(is_pandigital(i), is_pandigital(9)))
            break
    print((time.time() - start_time) * 1000)


def is_pandigital1(x):
    m = x
    l = len(str(x))
    d = set(str(x))
    if len(d) < l and '0' in d:
        return False
    j = 1
    while True:
        m += x
        l += len(str(m))
        d |= set(str(m))
        if '0' in d or len(d) < l:
            return False
        j += 1
        if len(d) == 9:
            return int(''.join(str(jj * x) for jj in range(1, j + 1)))


if __name__ == "__main__":
    main(is_pandigital)
    main(is_pandigital1)
