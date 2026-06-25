# Question 2: List Operations

# a. Find the largest number in a list
numbers = [12, 45, 67, 23, 89, 34]
print("Largest Number:", max(numbers))

# b. Remove duplicates from a list
duplicate_list = [1, 2, 3, 2, 4, 1, 5]
unique_list = list(set(duplicate_list))
print("List after removing duplicates:", unique_list)

# c. Count how many even numbers are in a list
num_list = [1, 2, 3, 4, 5, 6, 8, 10]
even_count = sum(1 for num in num_list if num % 2 == 0)
print("Number of even elements:", even_count)

# d. Input 5 numbers and store them in a list
user_list = []

for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    user_list.append(num)

print("Entered List:", user_list)

# e. Function that returns the average of all numbers in a list
def calculate_average(lst):
    return sum(lst) / len(lst)

print("Average:", calculate_average(user_list))

# f. Convert a string into a list of characters using list()
text = "Python"
char_list = list(text)
print("List of Characters:", char_list)

# g. Join all elements of a list into a single string using join()
words = ["Python", "is", "easy", "to", "learn"]
joined_string = " ".join(words)
print("Joined String:", joined_string)
