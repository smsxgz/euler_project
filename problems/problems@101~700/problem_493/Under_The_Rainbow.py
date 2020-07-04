def solve(n):
    previous_porbs = [1, 0, 0, 0, 0, 0, 0, 0]
    for i in range(n):
        current_probs = [0] * 8

        for j in range(1, 8):
            current_probs[j] = 10 * (8 - j) / (70 - i) * previous_porbs[
                j - 1] + (10 * j - i) / (70 - i) * previous_porbs[j]

        previous_porbs = current_probs

    res = 0
    for j in range(1, 8):
        res += j * previous_porbs[j]

    return res


if __name__ == "__main__":
    print(solve(20))
