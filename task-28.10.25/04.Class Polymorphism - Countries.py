# Class Polymorphism - Countries
class Country:
    def __init__(self, name):
        """Constructor to describe country name"""
        self.name = name
        print(f"Country name: {self.name}")
    
    def capital(self):
        """Method to describe capital"""
        pass
    
    def language(self):
        """Method to describe language"""
        pass

class India(Country):
    def __init__(self):
        super().__init__("India")
    
    def capital(self):
        return "The capital of India is New Delhi"
    
    def language(self):
        return "The primary language of India is Hindi (with many regional languages)"

class USA(Country):
    def __init__(self):
        super().__init__("United States of America")
    
    def capital(self):
        return "The capital of USA is Washington, D.C."
    
    def language(self):
        return "The primary language of USA is English"

class UK(Country):
    def __init__(self):
        super().__init__("United Kingdom")
    
    def capital(self):
        return "The capital of UK is London"
    
    def language(self):
        return "The primary language of UK is English"

# Main program
print("=== Country Polymorphism Demo ===\n")

print("Choose a country to learn about:")
print("1. India")
print("2. USA")
print("3. UK")
print("4. All Countries")

choice = int(input("\nEnter your choice (1-4): "))
print()

if choice == 1:
    country = India()
    print(country.capital())
    print(country.language())

elif choice == 2:
    country = USA()
    print(country.capital())
    print(country.language())

elif choice == 3:
    country = UK()
    print(country.capital())
    print(country.language())

elif choice == 4:
    print("--- Information about all countries ---\n")
    countries = [India(), USA(), UK()]
    for country in countries:
        print(country.capital())
        print(country.language())
        print()

else:
    print("Invalid choice!")
