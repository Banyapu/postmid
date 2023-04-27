import random

n = 5
d1 = []
d2 = []
high_rolls = []

for num in range(1, n + 1):
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    d1 = d1 + [roll1]
    d2 = d2 + [roll2]
    if roll1 + roll2 >= 6:
        high_rolls = high_rolls + [num]

print("Dice 1: ", d1)
print("Dice 2: ", d2)
if high_rolls:
    print("High rolls occurred on the following rolls: ", high_rolls)
else:
    print("No high rolls occurred.")
