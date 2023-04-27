data = [((1, 2), (3, 4)), ((5, 6), (7, 8))]
for item in data:
    x = lambda a, b: sum(a) + sum(b)
    print(x(item[0], item[1]), end=" ")
