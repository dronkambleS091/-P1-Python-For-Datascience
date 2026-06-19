numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print("Original List:", numbers)

print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Average:", sum(numbers) / len(numbers))

print("Ascending Order:", sorted(numbers))
print("Descending Order:", sorted(numbers, reverse=True))

numbers.append(110)
print("After Adding Number:", numbers)

numbers.pop(0)
print("After Removing First Item:", numbers)
