DICT = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def to_roman(num):
    ints = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    nums = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV',
            'I')
    result = []
    for i in range(len(ints)):
        count, num = divmod(num, ints[i])
        result.append(nums[i] * count)
    return ''.join(result)


def to_num(rom):
    num = 0
    idx = 0
    while idx < len(rom):
        if idx < len(rom) - 1 and DICT[rom[idx]] < DICT[rom[idx + 1]]:
            num += DICT[rom[idx + 1]] - DICT[rom[idx]]
            idx += 2
        else:
            num += DICT[rom[idx]]
            idx += 1
    return num


if __name__ == "__main__":
    with open('p089_roman.txt', 'r') as f:
        res = 0
        for line in f.readlines():
            line = line.strip()
            res += len(line) - len(to_roman(to_num(line)))
        print(res)
