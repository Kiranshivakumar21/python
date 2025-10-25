from datetime import datetime

now = datetime.now()
milliseconds = int(now.timestamp() * 1000)
print("Current time in milliseconds:", milliseconds)

