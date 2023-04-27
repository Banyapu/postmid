def print_digit(a_string):
    res = " "
    for ch in a_string:
        cond1 = "0" <= ch <= "9"
        cond2 = ch in "0123456789"
        cond3 = ch in "aeiouAEIOU"
        if cond3:
            res = res + ch + " "
    print(res)


print_digit("24 hours in 1 day, 7 days in a 1 week.")
message = "I met a man with 7 wives. Each wife had 7 sacks."
print_digit(message)
