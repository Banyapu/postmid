sum = 0
for x in range(1, 4, 2):
    for y in range(2, 5, 2):
        for z in range(1, 2, 1):
            sum += (x + y) * z
print(sum)
