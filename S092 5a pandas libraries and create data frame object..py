import pandas as pd

# Read Excel file
df = pd.read_excel("StressLevelDataset.xlsx")

# Display first 5 rows
print("Stress Level Dataset:")
print(df.head())

# Display DataFrame information
print("\nShape of Dataset:", df.shape)
print("\nColumns:")
print(df.columns)
