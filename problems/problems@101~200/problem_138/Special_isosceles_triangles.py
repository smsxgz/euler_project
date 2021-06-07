# (x, L) is the solution to the equation x^2 - 5 * L^2 = -1
# The base solution is (38, 17)
# The base solution to the eqaution x^2 - 5 * L^2 = 1 is (9, 4)

x, L = 38, 17
x0, y0 = 9, 4

s = L
for _ in range(11):
    x, L = x * x0 + 5 * L * y0, x * y0 + L * x0
    s += L
print(s)
