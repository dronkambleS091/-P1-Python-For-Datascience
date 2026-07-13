import time
from datetime import datetime

timestamp = time.time()

date = datetime.fromtimestamp(timestamp)

print("Timestamp:", timestamp)
print("Date:", date.strftime("%d-%m-%Y %H:%M:%S"))
