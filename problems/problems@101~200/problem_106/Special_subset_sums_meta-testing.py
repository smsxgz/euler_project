from math import factorial


def count(k):
    # count the number of {a_1 < ... < a_k, b_1 < ... < b_3, a_i < b_i, i = 1, ..., k}
    # {a_1, ..., a_k, b_1, ..., b_k} = {1, 2, ..., 2k}

    dp = [1]
    for _ in range(k - 1):
        s = 0
        new_dp = []
        for d in dp:
            s += d
            new_dp.append(s)
        new_dp.append(s)
        dp = new_dp
    return sum(dp)


def main(n):
    k = n // 2
    res = 0
    for i in range(2, k + 1):
        c = factorial(n) // factorial(2 * i) // factorial(n - 2 * i)
        res += c * (factorial(2 * i) // factorial(i)**2 // 2 - count(i))
    print(res)


if __name__ == "__main__":
    main(4)
    main(7)
    main(12)
