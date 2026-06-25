# 2a. Nested Tuple
nested_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print("Nested Tuple:", nested_tuple)

# 2b. Sort Nested Tuple
nested_tuple2 = ((3, 4), (1, 2), (5, 6))
sorted_tuple = tuple(sorted(nested_tuple2))
print("Sorted Nested Tuple:", sorted_tuple)

# 2c. Clone List
original_list = [10, 20, 30, 40, 50]
cloned_list = original_list.copy()
print("Original List:", original_list)
print("Cloned List:", cloned_list)

# 2d. Check Tuple Immutability
my_tuple = (10, 20, 30)

try:
    my_tuple[1] = 34
except TypeError as e:
    print("Tuple is immutable.")
    print("Error:", e)
