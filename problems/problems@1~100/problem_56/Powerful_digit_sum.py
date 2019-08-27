def digit_sum(n):
    res = 0
    while n > 0:
        res += n % 10
        n = n // 10
    return res


max_digit_sum = 1
for i in range(2, 100):
    power = 1
    for j in range(1, 100):
        power *= i
        max_digit_sum = max(digit_sum(power), max_digit_sum)

max_digit_sum
