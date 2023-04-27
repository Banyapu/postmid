list1 = []
list1.append(4)
list1.extend(list(range(6, 8)))
list1 += list1
list1.remove(6)
list1.clear()
list1.insert(0, "10")
list1.append(list1.count(10))
list1 = [int(x) for x in list1]
list1 *= 2
print(sorted(list1))
