theta = 0
d = 1

a1 = 2
c1 = (1, 0)
while True:
    x = a1 + a1 * (c1[0] * theta - d * c1[1]) // d
    y = a1 + a1 * (c1[0] * (theta + 1) - d * c1[1]) // d
    for i in range(x, y + 1):
        theta1 = theta * 10**(len(str(i))) + i
        d1 = d * 10**(len(str(i)))

        if a1 + a1 * (c1[0] * theta1 - d1 * c1[1]) // d1 == i:
            theta = theta1
            d = d1
            c1 = (a1 * c1[0], a1 * c1[1] + i - a1)
            a1 = i
            break

    print(theta, d, a1, c1)
    if len(str(theta)) > 24:
        print(len(str(theta)))
        break
