import ray
from mylib import Miller_Rabin
ray.init()


@ray.remote
def test(n1, n2):
    n = n1
    t = 2 * n * n - 1
    count = 0
    while n <= n2:
        count += Miller_Rabin(t)
        n += 1
        t += 4 * n - 2

    return count


res = ray.get(
    [test.remote(2, 10000)] +
    [test.remote(10000 * i + 1, 10000 * (i + 1)) for i in range(1, 5000)])
print(sum(res))
