import numpy as np
from cvxopt import matrix
from cvxopt.glpk import ilp


def number2vector(n_str):
    m = np.zeros(len(n_str) * 10, dtype="int")
    for i, a in enumerate(n_str):
        m[10 * i + int(a)] = 1
    return m


def vector2number(m):
    m = m.reshape(-1, 10)
    s = "".join([str(i) for i in np.argmax(m, axis=1)])
    return s


guesses = []
nums = []
with open("./guess.txt", "r") as f:
    for line in f.readlines():
        line = line.split(" ;")
        nums.append(int(line[1][0]))
        guesses.append(line[0])
# guesses = sorted(guesses, key=lambda x: x[1])
n = len(guesses[0])
print(guesses)


c = matrix(np.ones(n * 10, dtype="int"), tc="d")
A = [number2vector(g) for g in guesses]
b = nums.copy()
for i in range(n):
    a = np.zeros(n * 10, dtype="int")
    for j in range(10):
        a[i * 10 + j] = 1
    A.append(a)
    b.append(1)
A = matrix(np.array(A, dtype="int"), tc="d")
b = matrix(b, tc="d")


G = matrix(-np.eye(n * 10), tc="d")
h = matrix(np.zeros(n * 10, dtype="int"), tc="d")


status, x = ilp(c, G, h, A, b, I=set(range(n * 10)))
print(status)
x = np.array(x).reshape(-1)
print(vector2number(x))
