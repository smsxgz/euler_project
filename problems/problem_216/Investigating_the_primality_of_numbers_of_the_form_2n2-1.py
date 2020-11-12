from mylib import Miller_Rabin

n = 2
t = 7
count = 1

N = 50000000
# N = 10000

while n <= N:
    t += 4 * n + 2
    n += 1
    count += Miller_Rabin(t)

    if n % 100000 == 0:
        print(n, count)

print(count)
