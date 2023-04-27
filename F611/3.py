n = 0
sum = 0
data = [22, 7, 24, 59, 10, 9, -1]
for x in data:
    while x >= 0:
        if sum < 100:
            n += 1
            sum += x
        break
print(n, sum)
