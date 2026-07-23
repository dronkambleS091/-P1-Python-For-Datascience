import numpy as np

arr = np.array([12, 45, 67, 23, 89, 34, 89])

# Find the maximum value
max_value = np.max(arr)

# Filter array to return only the maximum value(s)
filter_arr = arr[arr == max_value]

print("Original Array:", arr)
print("Maximum Value:", max_value)
print("Filtered Array:", filter_arr)
