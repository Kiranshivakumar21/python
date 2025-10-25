from datetime import datetime

dt1 = input("Enter first datetime (YYYY-MM-DD HH:MM:SS): ")
dt2 = input("Enter second datetime (YYYY-MM-DD HH:MM:SS): ")
d1 = datetime.strptime(dt1, "%Y-%m-%d %H:%M:%S")
d2 = datetime.strptime(dt2, "%Y-%m-%d %H:%M:%S")
diff = d2 - d1
days = diff.days
hours, rem = divmod(diff.seconds, 3600)
minutes, seconds = divmod(rem, 60)
print(f"Difference: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")
