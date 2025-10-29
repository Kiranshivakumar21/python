from datetime import datetime

class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob  # Date format: "YYYY-MM-DD"
    
    def age(self):
        birth_date = datetime.strptime(self.dob, "%Y-%m-%d")
        today = datetime.now()
        age = today.year - birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1
        return age

# Test examples
person1 = Person("Kiran", "India", "2001-02-21")
print(f"Name: {person1.name}")
print(f"Country: {person1.country}")
print(f"Age: {person1.age()} years")
print(" "*25)
person2 = Person("Bharathi", "India", "2003-01-01")
print(f"Name: {person2.name}")
print(f"Country: {person2.country}")
print(f"Age: {person2.age()} years")
