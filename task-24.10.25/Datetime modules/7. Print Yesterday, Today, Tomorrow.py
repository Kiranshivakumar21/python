from datetime import datetime, timedelta

date_in = input("Enter date (YYYY-MM-DD): ")
dt = datetime.strptime(date_in, "%Y-%m-%d")
print("Yesterday:", (dt - timedelta(days=1)).date())
print("Today:", dt.date())
print("Tomorrow:", (dt + timedelta(days=1)).date())
