def euler686(L, n, prec=200):
    from gmpy2 import get_context, log, ceil
    get_context().precision = prec
    log10 = log(10)
    lb = log(L) / log10 % 1
    ub = log(L + 1) / log10 % 1
    l = (log(L + 1) - log(L)) / log10
    x0 = log(2) / log10
    x = x0
    a = int(x)
    x -= a
    k, k0 = 1, 0
    # determine the first convergent with smaller error than l
    while True:
        x = 1 / x
        a = int(x)
        x -= a
        k, k0 = a * k + k0, k
        k_err = mod1(k * x0)
        if abs(k_err) < l:
            break
    x = 1 / x
    a = int(x)
    x -= a
    # determine the first semi-convergent with smaller error than l
    kk = k0
    for m in range(1, a + 1):
        kk += k
        kk_err = mod1(kk * x0)
        if abs(kk_err) < l:
            break
    dLst = [k, kk, k + kk]  # exponent differences
    ### determine a solution
    if k_err > 0:
        e = k * int(ceil(lb / k_err))
    elif kk_err > 0:
        e = kk * int(ceil(lb / kk_err))
    else:
        raise ValueError
    ### move backwards until we find the smallest solution
    # find convergents < e
    kLst = []
    while k < e:
        k, k0 = a * k + k0, k
        if k >= e:
            break
        kLst += [k]
        x = 1 / x
        a = int(x)
        x -= a
    # use convergent to move backwards in big steps
    for d in kLst[::-1]:
        while e > d:
            x = (e - d) * x0 % 1
            if (lb < ub and x >= lb and x < ub) or (lb > ub and x > ub
                                                    and x <= lb):
                e -= d
            else:
                break
    print(e)
    # then use exponent differences to move backwards in small steps
    while True:
        for d in dLst:
            if d >= e:
                continue
            x = (e - d) * x0 % 1
            if (lb < ub and x >= lb and x < ub) or (lb > ub and x > ub
                                                    and x <= lb):
                e -= d
                break
        else:
            break

    print(e)
    c = 1
    while True:
        for d in dLst:
            x = (e + d) * x0 % 1
            if (lb < ub and x >= lb and x < ub) or (lb > ub and x > ub
                                                    and x <= lb):
                e += d
                c += 1
                if c == n:
                    return e
                break


def mod1(x):
    x -= int(x)
    if x > 0.5:
        x -= 1
    return x


if __name__ == '__main__':
    print(euler686(123, 678910))