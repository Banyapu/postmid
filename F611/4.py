data = [6, 4, 9, 3]
i = 3
while i > 0:
    if data[i] < data[i - 1]:
        data[i], data[i - 1] = data[i - 1], data[i]
    i -= 1
print(data)
