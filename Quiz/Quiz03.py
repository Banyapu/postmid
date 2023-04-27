m = int(input("Enter m: "))
total = 0
discount = 0
for i in range(m):
    p, n, s = input(f"Product {i+1} enter p n s: ").split()
    p = float(p)
    n = int(n)
    s = float(s)
    total = total + (p * n)
    discount = discount + n * (p * ((100 - s) / 100))
print(f"Total cost before sales: {total:.2f}")
print(f"Total cost after sales: {discount:.2f}")
