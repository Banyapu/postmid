x = 30  # global


def a1():
    x = 10  # local
    print(f"x = {x}")


def a2():
    x = 20  # local
    print(f"x = {x}")


def a3():
    print(f"x = {x}")


a1()
a2()
a3()
print(f"x = {x}")
