def printx(x):
    print(x)


def add100(x):
    for i in range(100):
        x = add1(x)
        if x % 2 == 1:
            printx(x)
    return x


def sub1(x):
    return x - 1


def add1(x):
    if 0 > x:
        return sub1(x)
    else:
        return x + 1


add100(0)
