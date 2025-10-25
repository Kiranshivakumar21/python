# Task 19: Find the number names contains with "Ku"
print("-" * 60)
print('Task 19: Find the number names contains with "Ku"')
print("-" * 60)

names = {"Kumar", "Kunal", "Rahul", "Priya", "Kushal", "Ankit", "Kusum", "Ravi", "Mukund"}
print("Set of names:", names)

names_with_ku = {name for name in names if "Ku" in name}
print('Names containing "Ku":', names_with_ku)
print('Number of names containing "Ku":', len(names_with_ku))
print()

