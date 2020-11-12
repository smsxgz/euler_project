# https://www.mathblog.dk/project-euler-89-develop-a-method-to-express-roman-numerals-in-minimal-form/

pattern = ['DCCCC', 'LXXXX', 'VIIII', 'CCCC', 'XXXX', 'IIII']
replacement = 'kk'


def saved_char(string):
    n = len(string)
    for p in pattern:
        string = string.replace(p, replacement)
    return n - len(string)


if __name__ == "__main__":
    with open('p089_roman.txt', 'r') as f:
        res = 0
        for line in f.readlines():
            res += saved_char(line.strip())
        print(res)
