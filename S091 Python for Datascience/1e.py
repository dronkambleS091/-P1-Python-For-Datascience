# Swap two elements in a list using function

def swap_list(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]
    return lst

numbers = [10, 20, 30, 40]

print("Original List:", numbers)

updated_list = swap_list(numbers, 1, 3)

print("Updated List:", updated_list)
