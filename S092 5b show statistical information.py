import pandas as pd

# Read Excel file
df = pd.read_excel("StressLevelDataset.xlsx")

# Statistical summary
print("Statistical Information:")
print(df.describe())

# Additional information
print("\nDataset Information:")
print(df.info())
print("S092 Dron Kamble")
