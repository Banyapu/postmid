t, n = input("Enter t n: ").split()
t = int(t)
n = int(n)

for num in range(n):
    b = int(input(f"Enter data {num+1}: "))
if b > t:
    print(f"Number of data greater than {t} is: {num+1} ")
if b < t:
    print(f"Number of data greater than {t} is: 0 ")
