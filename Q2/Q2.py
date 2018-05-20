import math


def fib(n):
    sq5 = math.sqrt(5)
    a = 1.0 / sq5
    b = (1.0 + sq5) / 2.0
    c = (1.0 - sq5) / 2.0
    return a * (math.pow(b, n) - math.pow(c, n))


def geometric_series_sum(const, n):
    return (1 - math.pow(const, n)) / (1 - const)


def solver(i):
    k = ((i + 3) / 3)  # add 3 to compensate for a term we deleted in the closed form

    sq5 = math.sqrt(5)
    a = 1.0 / sq5
    b = (1.0 + sq5) / 2.0
    b = math.pow(b, 3)
    c = (1.0 - sq5) / 2.0
    c = math.pow(c, 3)
    res = a * (geometric_series_sum(b, k) - geometric_series_sum(c, k))
    return res


def max_fib_index(limit):
    i = 0
    for i in range(1000):
        if fib(i) > limit:
            return i-1


def sol1(limit):
    # closed form solution to the problem

    # find the index of the biggest fib number less than the limit
    i = max_fib_index(limit)

    return solver(i)


def sol2(limit):
    res = 0
    a = 1
    b = 1
    c = a + b
    while c < limit:
        res = res + c
        a = b + c
        b = c + a
        c = a + b
    return res


limit = 4000000
print(sol1(limit))
print(sol2(limit))
