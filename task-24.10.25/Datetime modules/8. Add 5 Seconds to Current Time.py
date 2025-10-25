from datetime import datetime, timedelta

now = datetime.now()
later = now + timedelta(seconds=5)
print("Current Time:", now.time())
print("Time after 5 seconds:", later.time())
