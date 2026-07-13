from datetime import datetime

date1 = datetime.strptime("15-07-2026", "%d-%m-%Y")
date2 = datetime.strptime("30-07-2026", "%d-%m-%Y")

if date1 > date2:
    print("Date1 is later than Date2")
elif date1 < date2:
    print("Date1 is earlier than Date2")
else:
    print("Both dates are the same")
