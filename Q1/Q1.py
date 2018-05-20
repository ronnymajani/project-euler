def sol1(limit):
    return sum([x for x in range(limit) if ((x % 5 == 0) or (x % 3 == 0))])


def sol2(limit):
    res = 0
    # multiples of 5
    i = 1
    while True:
        mult_5 = 5 * i
        if mult_5 < limit:
            res += mult_5
            i += 1
        else:
            break
    # multiples of 3
    i = 1
    j = 1
    while True:
        mult_3 = 3*i
        if mult_3 < limit:
            res += mult_3
            i += 1
            j += 1
            # eliminate repeated numbers
            if j == 5:
                i += 1
                j = 1
        else:
            break
    return res


def sol2_opt1(limit):
    res = 0
    # multiples of 5
    lim_mutiplier_5 = limit//5
    if lim_mutiplier_5 * 5 == limit:
        lim_mutiplier_5 -= 1

    for i in range(1, lim_mutiplier_5+1):
        mult_5 = 5 * i
        res += mult_5

    # multiples of 3
    lim_mutiplier_3 = limit // 3
    if lim_mutiplier_3 * 3 == limit:
        lim_mutiplier_3 -= 1
    j = 1
    for i in range(1, lim_mutiplier_3 + 1):
        if j == 5:
            j = 1
            continue
        mult_3 = 3*i
        res += mult_3
        j += 1

    return res


def sol2_opt2(limit):
    res = 0
    # add multiples of 5
    lim_mutiplier_5 = limit//5
    if lim_mutiplier_5 * 5 == limit:
        lim_mutiplier_5 -= 1

    for i in range(1, lim_mutiplier_5+1):
        mult_5 = 5 * i
        res += mult_5

    # add multiples of 3
    lim_mutiplier_3 = limit // 3
    if lim_mutiplier_3 * 3 == limit:
        lim_mutiplier_3 -= 1
    for i in range(1, lim_mutiplier_3 + 1):
        mult_3 = 3*i
        res += mult_3

    # subtract multiples of 15
    lim_mutiplier_15 = limit // 15
    if lim_mutiplier_15 * 3 == limit:
        lim_mutiplier_15 -= 1
    for i in range(1, lim_mutiplier_15 + 1):
        mult_15 = 15 * i
        res -= mult_15

    return res


def sol3(limit):
    lim_mutiplier_5 = limit // 5
    if lim_mutiplier_5 * 5 == limit:
        lim_mutiplier_5 -= 1
    lim_mutiplier_3 = limit // 3
    if lim_mutiplier_3 * 3 == limit:
        lim_mutiplier_3 -= 1
    lim_mutiplier_15 = limit // 15
    if lim_mutiplier_15 * 3 == limit:
        lim_mutiplier_15 -= 1

    arithmeticSum_5 = (lim_mutiplier_5 * (lim_mutiplier_5 + 1)) / 2
    arithmeticSum_3 = (lim_mutiplier_3 * (lim_mutiplier_3 + 1)) / 2
    arithmeticSum_15 = (lim_mutiplier_15 * (lim_mutiplier_15 + 1)) / 2

    res = 5*arithmeticSum_5 + 3*arithmeticSum_3 - 15*arithmeticSum_15
    return int(res)


print(sol1(1000))
print(sol2(1000))
print(sol2_opt1(1000))
print(sol2_opt2(1000))
print(sol3(1000))
