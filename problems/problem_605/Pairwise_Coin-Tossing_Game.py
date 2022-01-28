# The probability of the stopping time being k is (k - 1) 2^(-k).
# M_a(b) = 2^(a - b) (a + (2^a - 1)(b - 1)) / (2^a - 1)^2 for b neq 1.

from mylib import Miller_Rabin, power_mod

mod = 10**8

a = 10**8 + 7
b = 10**4 + 7
print(Miller_Rabin(10**8 + 7))

x = power_mod(2, a, mod) - 1

res = power_mod(2, a - b, mod)
res *= a + x * (b - 1)
res %= mod
res *= x * x
res %= mod
print(res)
