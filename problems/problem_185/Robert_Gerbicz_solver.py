guesses = []
nums = []
with open("./guess.txt", "r") as f:
    for line in f.readlines():
        line = line.split(" ;")
        nums.append(int(line[1][0]))
        guesses.append(line[0])
n = len(guesses)
print(guesses)

prefixs = [g[:8] for g in guesses]
suffixs = [g[8:] for g in guesses]


def same(n1, n2):
    r = 0
    for a, b in zip(n1, n2):
        if a == b:
            r += 1
    return r


N = 10 ** 8
pre_dict = dict()
pre_mem = set()
suf_dict = dict()
suf_mem = set()
for i in range(N):
    if i % 1000000 == 0:
        print(i)
    s = str(i)
    s = "0" * (8 - len(s)) + s

    Pre = []
    for idx, g in enumerate(prefixs):
        p = same(s, g)
        if p > nums[idx]:
            break
        Pre.append(p)
    else:
        key = tuple(Pre)
        if key in pre_mem:
            if key in pre_dict:
                pre_dict.pop(key)
        else:
            pre_mem.add(key)
            pre_dict[key] = s

    Suf = []
    for idx, g in enumerate(suffixs):
        p = same(s, g)
        if p > nums[idx]:
            break
        Suf.append(p)
    else:
        key = tuple(Suf)
        if key in suf_mem:
            if key in suf_dict:
                suf_dict.pop(key)
        else:
            suf_mem.add(key)
            suf_dict[key] = s


for pkey in pre_dict:
    skey = []
    for idx, p in enumerate(pkey):
        skey.append(nums[idx] - p)
    skey = tuple(skey)
    if skey in suf_dict:
        print(pre_dict[pkey] + suf_dict[skey])
