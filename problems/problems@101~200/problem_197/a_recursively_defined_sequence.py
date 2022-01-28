def func(x):
    t = 30.403243784
    return int(2**(t - x * x)) * 10**(-9)


x = 1
for i in range(1000):
    if i % 100 == 0:
        print(x, func(x))
    x = func(x)
