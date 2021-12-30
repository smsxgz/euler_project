from mylib import Mobius, sqrt

N = 10**14
sq = 10**7

mobius = Mobius(sq)

res = 0
for i in range(1, sq + 1):
    for j in range(1, sq // i + 1):
        res += mobius[i] * j * j * (N // (i * j)**2)

print(res)
