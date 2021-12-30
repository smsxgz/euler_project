from collections import Counter


def is_palindromic(n):
    n = str(n)
    return n == n[::-1]


def solver(N):
    counter = Counter()
    for i in range(1, N):
        i3 = i**3
        if i3 > N:
            break
        for j in range(1, N):
            n = j * j + i3
            if n > N:
                break
            counter[n] += 1

    nums = []
    for n in counter:
        if counter[n] == 4 and is_palindromic(n):
            nums.append(n)
    nums.sort()
    print(nums)


if __name__ == "__main__":
    solver(10**9)
