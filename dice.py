import random

n = 5
d1 = []
d2 = []
high_rolls = []

for num in range(n):
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    d1.append(roll1)
    d2.append(roll2)
    if roll1 + roll2 >= 6:
        high_rolls.append(num + 1)

print("Dice 1: ", d1)
print("Dice 2: ", d2)
if high_rolls:
    print("High rolls occurred on the following rolls: ", high_rolls)
else:
    print("No high rolls occurred.")
