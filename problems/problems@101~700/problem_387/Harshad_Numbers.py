from mylib import Miller_Rabin as is_prime


def strong_truncatable_numbers(k):
    nums = list(range(2, 10, 2))
    strong_nums = []

    for j in range(2, k + 1):
        tmp = []
        for n in nums:
            for i in range(10):
                m = 10 * n + i
                s = sum(int(s) for s in str(m))
                if m % s == 0:
                    tmp.append(m)
                    if is_prime(m // s):
                        strong_nums.append(m)
        nums = tmp

    return strong_nums


def main(k):
    nums = [18] + strong_truncatable_numbers(k - 1)
    res = []
    for n in nums:
        for i in [1, 3, 7, 9]:
            m = 10 * n + i
            if is_prime(m):
                res.append(m)
    return sum(res)


if __name__ == '__main__':
    from mylib import StopWatch

    print(main(4))

    with StopWatch():
        print(main(14))
