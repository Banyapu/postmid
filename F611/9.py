def myfn(t):
    return t[0][1:2]


data = [("cat", 2), ("dog", 3), ("ant", 4), ("fish", 1)]
data.sort(key=myfn)
for item in data:
    print(item[0], end=" ")
