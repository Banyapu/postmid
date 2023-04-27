def f(x):
    return [x[1], x[0]]


list1 = [[1, "d"], [2, "c"], [3, "b"], [4, "a"]]
list2 = [f(x) for x in list1]
print(list2)
