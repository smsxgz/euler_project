from mylib import inverse_mod

seq = "UDDDUdddDDUDDddDdDddDDUDDdUUDd" [::-1]

s = (1, 0, 1)
for ch in seq:
    if ch == 'D':
        s = (s[0] * 3, s[1] * 3, s[2])
    elif ch == 'U':
        s = (s[0] * 3, s[1] * 3 - s[2] * 2, s[2] * 4)
    elif ch == 'd':
        s = (s[0] * 3, s[1] * 3 + s[2], s[2] * 2)

a, b, c = s
k = (-(b % c) * inverse_mod(a % c, c)) % c
m = (a * k + b) // c
n = ((10**15 - m) // a + 1) * a + m
print(n)
