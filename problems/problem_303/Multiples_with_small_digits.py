# from mylib import euler_prime


def small_digits_number_generator():
    s = 0
    while True:
        s += 1
        t = s
        n = 0
        q = 1
        while t > 0:
            t, r = divmod(t, 3)
            n += q * r
            q *= 10
        yield n


def solver(n):
    nums = list(range(1, n + 1))
    res = 0
    for n in small_digits_number_generator():
        tmp = []
        for m in nums:
            if n % m == 0:
                tmp.append(m)
                res += n // m
                if m in [999, 4995, 7992, 9990, 9999]:
                    print(n, m, nums)
        for m in tmp:
            nums.remove(m)

        if len(nums) == 1:
            break

    print(res)
    print(res + 11112222222222222222 // 9999)


if __name__ == "__main__":
    solver(10000)
