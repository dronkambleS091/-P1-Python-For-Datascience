from datetime import datetime

now = datetime.now()

print("DD-MM-YYYY:", now.strftime("%d-%m-%Y"))
print("MM/DD/YYYY:", now.strftime("%m/%d/%Y"))
print("Month Day, Year:", now.strftime("%B %d, %Y"))
print("Day-Month-Year:", now.strftime("%A, %d %B %Y"))
