from abc import ABC, abstractmethod

# Abstract class Animal
class Animal(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def sound(self):
        """Abstract method that must be implemented by subclasses"""
        pass

# Lion class inheriting from Animal
class Lion(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def sound(self):
        return f"{self.name} the Lion says: ROAR! ROAR!"

# Tiger class inheriting from Animal
class Tiger(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def sound(self):
        return f"{self.name} the Tiger says: GROWL! GROWL!"

# Main program
print("=== Abstract Class Animal Demo ===\n")

# Get user input for Lion
lion_name = input("Enter the Lion's name: ")
lion = Lion(lion_name)
print(lion.sound())

print()

# Get user input for Tiger
tiger_name = input("Enter the Tiger's name: ")
tiger = Tiger(tiger_name)
print(tiger.sound())

print("\n--- Demonstrating Abstraction ---")
# Create a list of animals
animals = [lion, tiger]
for animal in animals:
    print(animal.sound())
