from mylib import euler_func, gcd, power_mod


def main():
    euler = euler_func(100000)
    n = 3
    res = []
    while len(res) < 25:
        n += 1

        if euler[n] == n - 1:
            continue

        if n % 3 == 0:
            continue

        q = gcd(n - 1, euler[n])
        if power_mod(10, q, n) == 1:
            res.append(n)
    print(sum(res))


if __name__ == "__main__":
    main()
