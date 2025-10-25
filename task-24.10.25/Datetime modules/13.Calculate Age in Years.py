from datetime import date

date_in = input("Enter birthdate (YYYY-MM-DD): ")
birthdate = date.fromisoformat(date_in)
today = date.today()
age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
print("Age:", age)
