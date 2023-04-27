s1 = "Today is 27-04-2566"
day, month, year = s1.split()[2].split("-")
new_s1 = f"Today is {year}-{month}-{day}"
print(new_s1)
