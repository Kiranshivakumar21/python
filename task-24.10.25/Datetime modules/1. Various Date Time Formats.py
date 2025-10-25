from datetime import datetime

now = datetime.now()
print("a) Current date and time:", now)
print("b) current date:", now.strftime("%F"))
print("c) Current year:", now.year)
print("d) Month of year:", now.month)
print("e) Week number of the year:", now.strftime("%U"))
print("f) Weekday of the week:", now.strftime("%A"))
print("e) Day of year:", now.strftime("%j"))
print("g) Day of the month:", now.day)
print("h) current Time:", now.time())
print("i) current time of hour:", now.strftime("%H"))
print("j) current time of minute:", now.strftime("%M"))
print("k) current time of second:", now.strftime("%S"))
print("l) current time of microsecond:", now.strftime("%f"))
print("m) current time is AM (or) PM:", now.strftime("%p"))





