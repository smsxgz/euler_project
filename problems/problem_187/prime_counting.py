from mylib import sqrt, euler_prime


def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid

    return high


N = 10**8
sq = sqrt(N)
prime = euler_prime(sq)

phi_cache = dict()


def phi(x, a):
    # print(x, a)
    if (x, a) in phi_cache:
        return phi_cache[(x, a)]
    if a == 1:
        return (x + 1) // 2

    t = phi(x, a - 1) - phi(x // prime[a - 1], a - 1)
    phi_cache[(x, a)] = t
    return t


pi_cache = dict()
pi_cache[1] = 0
pi_cache[2] = 1


def pi(x):
    if x < sq:
        return binary_search(prime, x) + 1

    # print(x)
    a = pi(sqrt(x))
    return phi(x, a) + a - 1


# print(pi(N // 2))

count = 0
for p in prime:
    count += pi(N // p) - pi(p) + 1

print(count)
