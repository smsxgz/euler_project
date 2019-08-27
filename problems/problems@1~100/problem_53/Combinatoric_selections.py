nums = [1]

for i in range(9):
    nums.append(nums[-1] * (23 - i) // (i + 1))

s = 23 + 1 - 2 * len(nums)

for j in range(24, 101):
    tmp = [1]
    for i in range(len(nums) - 1):
        t = nums[i] + nums[i + 1]
        if t > 1000000:
            break
        tmp.append(t)
    nums = tmp
    s += j + 1 - 2 * len(nums)
s
