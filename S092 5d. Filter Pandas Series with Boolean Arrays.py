import pandas as pd

# Read Excel file
df = pd.read_excel("Stress_Dataset.xlsx")

# Create Series from Age column
age_series = pd.Series(df["Age"])

print("Original Age Series:")
print(age_series)

# Boolean filtering (Age greater than 20)
filtered_series = age_series[age_series > 20]

print("\nFiltered Series (Age > 20):")
print(filtered_series)
print("S092 Dron Kamble")

