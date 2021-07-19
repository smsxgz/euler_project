from mylib import gcd


def permutations(lst, prefix=[]):
    if len(lst) == 0:
        yield prefix
        return

    for i in range(len(lst)):
        yield from permutations(lst[:i] + lst[i + 1:], prefix + [lst[i]])
    return


def slice(lst, path=[], d=None):
    if d == 1:
        return

    if len(lst) == 0:
        yield path, d
        return

    if lst[0] == '0':
        return

    for i in range(len(lst)):
        n = int(''.join(lst[:i + 1]))
        if d is None:
            d1 = n
        else:
            d1 = gcd(d, n)
        yield from slice(lst[i + 1:], path + [n], d1)
    return


# def slice(lst):
#     for i in range(9):
#         if lst[i + 1] == '0':
#             continue
#         n1 = int(''.join(lst[:i + 1]))
#         n2 = int(''.join(lst[i + 1:]))
#         d = gcd(n1, n2)
#         if d > 1:
#             yield [n1, n2], d


def solve(lst):
    for nums, d in slice(lst):
        if len(nums) == 1:
            continue
        for i in range(2, d + 1):
            if d % i == 0:
                s = str(i)
                for n in nums:
                    s += str(n // i)
                # print(s, nums)
                if len(set(s)) == 10 and len(s) == 10:
                    print(nums, i)
                    return True
    return False


for lst in permutations('9876543210'):
    if solve(lst):
        print(lst)
        break
