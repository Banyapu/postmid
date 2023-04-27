def up():
    global x
    x += 1


def down():
    global x
    x -= 1


x = 0
n = 10
while n > 0:
    if n % 2 == 0:
        up()
    else:
        down()
    n //= 2
    print(x, end="")
