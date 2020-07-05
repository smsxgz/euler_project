mod = 1000000

two_partition = [0, 0, 1]
two_partition_sum = [0, 0, 1]

n = 3
p = 1
while True:
    par = (two_partition[n - 1] + p + two_partition_sum[n - 3]) % mod

    two_partition.append(par)
    two_partition_sum.append((two_partition_sum[n - 1] + par) % mod)

    m = 2 * (n - 1)
    two_pal = (p + two_partition_sum[n - 3] + two_partition[n - 1]) % mod
    if two_pal == 0:
        print(m)
        break

    m = 2 * n - 1
    two_pal = two_partition_sum[n - 1]
    if two_pal == 0:
        print(m)
        break

    n += 1
    p = p * 2 % mod
