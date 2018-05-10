res = set()

for i in range(2, 10):
    for j in range(1234, 9876 // i + 1):
        if len(set(str(j))) < 4:
            continue
        s = set(str(i)) | set(str(j)) | set(str(i * j))
        if len(s) == 9 and ('0' not in s):
            print(i, j, i * j)
            res.add(i * j)

for i in range(12, 99):
    if len(set(str(i))) < 2:
        continue
    for j in range(123, 9876 // i + 1):
        if len(set(str(j))) < 3:
            continue
        s = set(str(i)) | set(str(j)) | set(str(i * j))
        if len(s) == 9 and ('0' not in s):
            print(i, j, i * j)
            res.add(i * j)
sum(res)
