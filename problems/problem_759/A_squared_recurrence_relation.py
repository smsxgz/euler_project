# N = \floor{16 \log_2(10)}
N = 53
pow_list = []
p = 1
for _ in range(N):
    p *= 2
    pow_list.append(p - 1)


def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low < high:
        mid = (high + low + 1) // 2

        if arr[mid] < x:
            low = mid

        elif arr[mid] > x:
            high = mid - 1

        else:
            return mid

    return low


# T1: \sum_{i=0}^{n} g(i)
# n = 2**M-1
T1 = dict()
T1[0] = 0
for i in range(1, N + 1):
    T1[i] = 2 * T1[i - 1] + 2**(i - 1)


def compute_T1(n):
    if n == 0:
        return 0
    M = binary_search(pow_list, n) + 1
    p = pow_list[M - 1] + 1
    res = T1[M]
    res += compute_T1(n - p) + n - p + 1
    return res


# T2: \sum_{i=0}^{2^M-1} g(i)^2
# n = 2**M-1
T2 = dict()
T2[0] = 0
for i in range(1, N + 1):
    T2[i] = 2 * T2[i - 1] + 2 * T1[i - 1] + 2**(i - 1)


def compute_T2(n):
    if n == 0:
        return 0
    M = binary_search(pow_list, n) + 1
    n = n - pow_list[M - 1] - 1
    res = T2[M]
    res += compute_T2(n) + 2 * compute_T1(n) + n + 1
    return res


# T3: \sum_{i=0}^{2^M-1} i g(i)
# n = 2**M-1
T3 = dict()
T3[0] = 0
for i in range(1, N + 1):
    p = 2**(i - 1)
    T3[i] = 2 * T3[i - 1] + p * T1[i - 1] + p**2 + (p - 1) * p // 2


def compute_T3(n):
    if n == 0:
        return 0
    M = binary_search(pow_list, n) + 1
    p = pow_list[M - 1] + 1
    n = n - p
    res = T3[M]
    res += compute_T3(n) + p * (compute_T1(n) + n + 1) + n * (n + 1) // 2
    return res


# T4: \sum_{i=0}^{2^M-1} i g(i)^2
T4 = dict()
T4[0] = 0
for i in range(1, N + 1):
    p = 2**(i - 1)
    T4[i] = 2 * T4[i - 1] + p * (T2[i - 1] + 2 * T1[i - 1] + p)
    T4[i] += 2 * T3[i - 1] + (p - 1) * p // 2


def compute_T4(n):
    if n == 0:
        return 0
    M = binary_search(pow_list, n) + 1
    p = pow_list[M - 1] + 1
    n = n - p
    res = T4[M]
    res += p * (compute_T2(n) + 2 * compute_T1(n) + n + 1)
    res += compute_T4(n) + 2 * compute_T3(n) + n * (n + 1) // 2
    return res


# T5: \sum_{i=0}^{2^M-1} i^2 g(i)
T5 = dict()
T5[0] = 0
for i in range(1, N + 1):
    p = 2**(i - 1)
    T5[i] = 2 * T5[i - 1] + p**2 * (T1[i - 1] + p)
    T5[i] += 2 * p * (T3[i - 1] + p * (p - 1) // 2)
    T5[i] += p * (p - 1) * (2 * p - 1) // 6


def compute_T5(n):
    if n == 0:
        return 0
    M = binary_search(pow_list, n) + 1
    p = pow_list[M - 1] + 1
    n = n - p
    res = T5[M]
    res += p**2 * (compute_T1(n) + n + 1)
    res += 2 * p * (compute_T3(n) + n * (n + 1) // 2)
    res += compute_T5(n) + n * (n + 1) * (2 * n + 1) // 6
    return res


# T6: \sum_{i=0}^{2^M-1} i^2 g(i)^2
T6 = dict()
T6[0] = 0
for i in range(1, N + 1):
    p = 2**(i - 1)
    T6[i] = 2 * T6[i - 1] + p**2 * (T2[i - 1] + 2 * T1[i - 1] + p)
    T6[i] += 2 * p * (T4[i - 1] + 2 * T3[i - 1] + p * (p - 1) // 2)
    T6[i] += 2 * T5[i - 1] + p * (p - 1) * (2 * p - 1) // 6


def compute_T6(n):
    if n == 0:
        return 0
    M = binary_search(pow_list, n) + 1
    p = pow_list[M - 1] + 1
    n = n - p
    res = T6[M]
    res += p**2 * (compute_T2(n) + 2 * compute_T1(n) + n + 1)
    res += 2 * p * (compute_T4(n) + 2 * compute_T3(n) + n * (n + 1) // 2)
    res += compute_T6(n) + 2 * compute_T5(n) + n * (n + 1) * (2 * n + 1) // 6
    return res


print(compute_T6(10))
print(compute_T6(100))
print(compute_T6(10**16) % 1000000007)