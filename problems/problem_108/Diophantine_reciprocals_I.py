from mylib import sqrt


def factors(n):
    sieveLimit = sqrt(n)
    spf = [2 if i % 2 == 0 else i for i in range(n + 1)]
    for i in range(3, sieveLimit + 1, 2):
        if spf[i] == i:
            for m in range(i * i, n + 1, 2 * i):
                if spf[m] == m:
                    spf[m] = i

    fs = [0] * (n + 1)
    fs[1] = 1
    for i in range(2, n + 1):
        if spf[i] == i:
            fs[i] = 3
        else:
            p = spf[i]

            c = 0
            j = i
            while j % p == 0:
                j = j // p
                c += 1

            fs[i] = (2 * c + 1) * fs[j]

    return fs


if __name__ == "__main__":
    for i, f in enumerate(factors(1000000)):
        if f > 2000:
            print(i)
            print(f)
            break
