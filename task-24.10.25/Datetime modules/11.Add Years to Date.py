from datetime import date

def addYears(d, years):
    try:
        return d.replace(year=d.year + years)
    except ValueError:
        return d.replace(year=d.year+years, day=28)

date_in = input("Enter date (YYYY-MM-DD): ")
years = int(input("Enter years to add (can be negative): "))
dt = date.fromisoformat(date_in)
print("Updated date:", addYears(dt, years))

#Enter date: 2000-02-29
#Enter years: 1
#Sample Output:
#Updated date: 2001-02-28
