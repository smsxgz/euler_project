import numpy as np

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


def number2vector(n_str):
    m = np.zeros(len(n_str) * 10, dtype="int")
    for i, a in enumerate(n_str):
        m[10 * i + int(a)] = 1
    return m


def vector2number(m):
    m = m.reshape(-1, 10)
    s = "".join([str(i) for i in np.argmax(m, axis=1)])
    return s


A = np.array([number2vector(g) for g in guesses], dtype="int")
b = np.array(nums, dtype="int")


def dist(x):
    err = (A * x).sum(axis=1) - b
    return sum(abs(err))


def solve(num_try=20):
    x = np.zeros(n * 10, dtype="int")
    for i in range(n):
        x[i * 10 + np.random.randint(0, 10)] = 1
    e = dist(x)

    while e > 0:
        trys = []
        for _ in range(num_try):
            i = np.random.randint(0, n)
            tx = x.copy()
            tx[i * 10 : (i + 1) * 10] = 0
            tx[i * 10 + np.random.randint(0, 10)] = 1
            trys.append(tx)

        x = min(trys, key=dist)
        e = dist(x)
    return vector2number(x)


if __name__ == "__main__":
    from mylib import StopWatch

    with StopWatch():
        print(solve(20))

    with StopWatch():
        print(solve(30))
