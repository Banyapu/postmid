def myfn(t):
    return t[1], t[0]


list1 = [[1, 2], [3, 4], [5, 6], [7, 8]]
list2 = []
for item in list1:
    list2.append(myfn(item))
print(list2)
