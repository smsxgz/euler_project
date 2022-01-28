MAX = 10**8 - 1

x = 7
y = 5

res = 0

while x + y < MAX:
    res += MAX // (x + y)
    x, y = 3 * x + 4 * y, 3 * y + 2 * x

print(res)
