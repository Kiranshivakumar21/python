salary = float(input("Enter employee salary: "))
years = int(input("Enter years of service: "))

if years > 5:
    bonus = 0.05 * salary
    print("Net bonus amount is:", bonus)
else:
    print("No bonus (service <= 5 years)")
