from mylib import power_mod

mods = [2]
p = 2
for _ in range(15):
    p *= 2
    mods.append(p)

for _ in range(8):
    p = (p // 2) * 5
    mods.append(p)

print(mods[-1])

m = 1832
A = 0
for mod in mods:
    A = power_mod(1777, A, mod)
    m += 1

print(m)
print(A)
