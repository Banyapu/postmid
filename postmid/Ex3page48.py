def print_even(a_list):
    for x in a_list:
        cond1 = x % 2 == 0
        if cond1:
            print(x, end=" ")
    print()


print_even([1, 2, 3, 4, 5])

list_1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 20, 21, 20]
print_even(list_1)

list_2 = list(range(20, 0, -3))
print_even(list_2)
