def solve(N):
    res = set()
    t = 1
    while 2 * t * (t + 1) <= N:
        k = 1
        while True:
            b = k * (t + k)
            a = t - 1 + b
            if a * b > N:
                break
            res.add(a * b)
            k += 1
        t += 1
    return len(res)


if __name__ == '__main__':
    from mylib import StopWatch
    with StopWatch():
        print(solve(10**14))
