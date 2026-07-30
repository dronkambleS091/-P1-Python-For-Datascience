import pandas as pd

# Read Excel file
df = pd.read_excel("Stress_Dataset.xlsx")

# Create dictionary using first 5 records
data_dict = dict(zip(df["Gender"].head(), df["Age"].head()))

# Create Pandas Series
series = pd.Series(data_dict)

print("Pandas Series created from Dictionary:")
print(series)
print("S092 Dron Kamble")
