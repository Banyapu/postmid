ch1 = input("Enter first character: ")
ch2 = input("Enter second character: ")
ch3 = input("Enter third character: ")
d1 = ord(ch3) - ord(ch1)
d2 = ord(ch3) - ord(ch2)
d1 = abs(d1)
d2 = abs(d2)
if ch1 <= ch3 <= ch2 or ch2 <= ch3 <= ch1:
    if d1 > d2:
        msg = f"{ch3} is closer to {ch2}."
    elif d1 < d2:
        msg = f"{ch3} is closer to {ch1}."
    else:
        msg = f"{ch3} is midway between {ch1} and {ch2}."
else:
    msg = f"{ch3} is not between {ch1} and {ch2}"
print(msg)
