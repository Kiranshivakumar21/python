# Class Polymorphism - Birds
class Bird:
    def __init__(self, name):
        """Constructor to describe bird name"""
        self.name = name
        print(f"Bird name: {self.name}")
    
    def make_sound(self):
        """Method to describe bird sound"""
        pass

class Parrot(Bird):
    def __init__(self, name):
        super().__init__(name)
    
    def make_sound(self):
        return f"{self.name} says: Squawk! Squawk! I can talk!"

class Sparrow(Bird):
    def __init__(self, name):
        super().__init__(name)
    
    def make_sound(self):
        return f"{self.name} says: Chirp! Chirp! Chirp!"

# Main program
print("=== Bird Polymorphism Demo ===\n")

# Get user input for Parrot
parrot_name = input("Enter the Parrot's name: ")
parrot = Parrot(parrot_name)
print(parrot.make_sound())

print()

# Get user input for Sparrow
sparrow_name = input("Enter the Sparrow's name: ")
sparrow = Sparrow(sparrow_name)
print(sparrow.make_sound())

print("\n--- Demonstrating Polymorphism ---")
# Polymorphism: same method name, different behavior
birds = [parrot, sparrow]
for bird in birds:
    print(bird.make_sound())
