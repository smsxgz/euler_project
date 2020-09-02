from mylib import combinations

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def extend(lst):
    if 6 in lst:
        if 9 not in lst:
            lst.append(9)
    if 9 in lst:
        if 6 not in lst:
            lst.append(6)


def testing(lst1, lst2):
    extend(lst1)
    extend(lst2)

    for num in [1, 4, 9, 16, 25, 36, 49, 64, 81]:
        i, j = divmod(num, 10)
        if (i in lst1 and j in lst2) or (i in lst2 and j in lst1):
            continue
        else:
            return False
    return True


com = list(combinations(digits, 6))
count = 0
for i in range(len(com)):
    lst1 = com[i]
    for j in range(i, len(com)):
        lst2 = com[j]
        if testing(lst1, lst2):
            count += 1

print(count)
