from datetime import datetime, timedelta

date_in = input("Enter date (YYYY-MM-DD): ")
dt = datetime.strptime(date_in, "%Y-%m-%d")
print("Current Date:", dt.date())
print("5 days before Current Date:", (dt - timedelta(days=5)).date())
