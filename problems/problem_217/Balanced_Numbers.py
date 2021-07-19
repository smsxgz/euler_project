N1 = dict()
S1 = dict()

N1[(1, 0)] = 0
S1[(1, 0)] = 0
for i in range(1, 10):
    N1[(1, i)] = 1
    S1[(1, i)] = i

for d in range(2, 24):
    for i in range(1, 9 * d + 1):
        N1[(d, i)] = sum(N1.get((d - 1, i - j), 0) for j in range(10))
        r = 0
        for j in range(10):
            r += 10 * S1.get((d - 1, i - j), 0) + j * N1.get((d - 1, i - j), 0)
        S1[(d, i)] = r

N2 = dict()
S2 = dict()

for i in range(10):
    N2[(1, i)] = 1
    S2[(1, i)] = i

for d in range(2, 24):
    for i in range(9 * d + 1):
        N2[(d, i)] = sum(N2.get((d - 1, i - j), 0) for j in range(10))
        r = 0
        for j in range(10):
            r += 10 * S2.get((d - 1, i - j), 0) + j * N2.get((d - 1, i - j), 0)
        S2[(d, i)] = r

mod = 3**15
T = 45
for D in range(2, 48):
    d = D // 2
    f = D - d * 2

    for i in range(1, 9 * d + 1):
        if f:
            T += S1[(d, i)] * (10 * N2[(d, i)]) * 10**(d + 1)
            T += 45 * (N1[(d, i)] * N2[(d, i)]) * 10**d
            T += S2[(d, i)] * (10 * N1[(d, i)])
        else:
            T += S1[(d, i)] * N2[(d, i)] * 10**d
            T += S2[(d, i)] * N1[(d, i)]

    T %= mod

print(T)
