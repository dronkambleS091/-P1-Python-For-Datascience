# Question 1: Tuple Operations

# a. Create a tuple with 5 different elements and print it
my_tuple = (10, 20, 30, 40, 50)
print("Original Tuple:", my_tuple)

# b. Access the first and last elements using indexing
print("First Element:", my_tuple[0])
print("Last Element:", my_tuple[-1])

# c. Slice a tuple and print the middle 3 elements
print("Middle 3 Elements:", my_tuple[1:4])

# d. Concatenate two tuples and print the result
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concat_tuple = tuple1 + tuple2
print("Concatenated Tuple:", concat_tuple)

# e. Reverse a tuple using slicing
print("Reversed Tuple:", my_tuple[::-1])

# f. Count how many times an element appears in a tuple
tuple_count = (1, 2, 3, 2, 4, 2, 5)
print("Count of 2:", tuple_count.count(2))

# g. Find the index of a specific element in a tuple
print("Index of 4:", tuple_count.index(4))

# h. Check if an element exists in a tuple
element = 3
if element in tuple_count:
    print(f"{element} exists in the tuple")
else:
    print(f"{element} does not exist in the tuple")

# i. Convert a list to a tuple
my_list = [100, 200, 300, 400]
converted_tuple = tuple(my_list)
print("Converted Tuple:", converted_tuple)

# j. Sort a tuple of numbers in ascending order
num_tuple = (9, 3, 7, 1, 5)
sorted_tuple = tuple(sorted(num_tuple))
print("Sorted Tuple:", sorted_tuple)

# k. Repeat a tuple 3 times using * operator
repeat_tuple = (1, 2, 3)
print("Repeated Tuple:", repeat_tuple * 3)

# l. Check immutability property of tuples
immutable_tuple = (10, 20, 30)

try:
    immutable_tuple[0] = 100
except TypeError as e:
    print("Tuple is immutable:", e)
