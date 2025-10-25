from datetime import datetime

date_str = input("enter a date like (21 June, 2018):")
dt = datetime.strptime(date_str, "%d %B, %Y")
print("Converted datetime:", dt)
