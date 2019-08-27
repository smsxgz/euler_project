def sqrt_digits(n, digits=10):
    queue = []
    while n > 0:
        queue.append(n % 100)
        n //= 100

    res = []
    a = 0
    r = 0
    for _ in range(digits):
        r *= 100
        a *= 10
        if queue:
            r += queue.pop(0)
        for i in range(10):
            u = 2 * a + 2 * i + 1
            if r >= u:
                r -= u
            else:
                res.append(i)
                break
        a += res[-1]
        if r == 0:
            return res
    return res


def main():
    res = 0
    for n in range(2, 100):
        s = sqrt_digits(n, 100)
        if len(s) == 100:
            res += sum(s)
    return res


if __name__ == '__main__':
    main()
