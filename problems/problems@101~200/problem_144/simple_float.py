def reflection(k1, k):
    return (2 * k - k1 + k * k * k1) / (1 + 2 * k * k1 - k * k)


def insection(k, x0, y0):
    x = (k * k * x0 - 2 * k * y0 - 4 * x0) / (4 + k * k)
    y = k * (x - x0) + y0
    return x, y


if __name__ == '__main__':
    k = -197 / 14
    x0, y0 = 1.4, -9.6

    hit = 0
    eps = 0.01
    while True:
        hit += 1
        k = reflection(k, y0 / (4 * x0))
        x0, y0 = insection(k, x0, y0)
        print(x0, hit)
        if abs(x0) <= eps and y0 > 0:
            print(hit)
            break
