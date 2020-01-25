def func(x):
    return x * x * x + 3*x -5


def false(m, n):
    if func(m) * func(n) >= 0:
        print("You have not assumed right a and b\n")
        return

    while abs(n - m) >= 0.0001:
        x0 = ((m * func(n)) - (n * func(m))) / (func(n) - func(m))

        if func(x0) == 0.0:
            break
        if (func(m) * func(x0)) < 0:
            n = x0
        else:
            m = x0
    print("root exist in : ", "%.8f" % x0)


a = 0.5
b = 0.6

false(a, b)
