x = 1


def main():
    x = 2
    print(a(x))


def a(w):
    global x
    x += 2
    return b() + 1, c(x)


def b(x=2):
    return c(x) * 2


def c(y=3):
    if y > x:
        return y**3
    else:
        return y**2


main()
