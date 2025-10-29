from abc import ABC, abstractmethod
import math

# Abstract class Shapes
class Shapes(ABC):
    @abstractmethod
    def volume(self):
        """Abstract method to calculate volume"""
        pass

# Cylinder class inheriting from Shapes
class Cylinder(Shapes):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
    
    def volume(self):
        vol = math.pi * self.radius ** 2 * self.height
        return round(vol, 2)

# Cone class inheriting from Shapes
class Cone(Shapes):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
    
    def volume(self):
        vol = (1/3) * math.pi * self.radius ** 2 * self.height
        return round(vol, 2)

# Sphere class inheriting from Shapes
class Sphere(Shapes):
    def __init__(self, radius):
        self.radius = radius
    
    def volume(self):
        vol = (4/3) * math.pi * self.radius ** 3
        return round(vol, 2)

# Main program
print("=== Abstract Class Shapes Demo (3D Volumes) ===\n")

print("Choose a 3D shape:")
print("1. Cylinder")
print("2. Cone")
print("3. Sphere")
print("4. All Shapes")

choice = int(input("\nEnter your choice (1-4): "))
print()

if choice == 1:
    radius = float(input("Enter the radius of the cylinder: "))
    height = float(input("Enter the height of the cylinder: "))
    cylinder = Cylinder(radius, height)
    print(f"\nCylinder with radius {radius} and height {height}:")
    print(f"Volume: {cylinder.volume()} cubic units")

elif choice == 2:
    radius = float(input("Enter the radius of the cone: "))
    height = float(input("Enter the height of the cone: "))
    cone = Cone(radius, height)
    print(f"\nCone with radius {radius} and height {height}:")
    print(f"Volume: {cone.volume()} cubic units")

elif choice == 3:
    radius = float(input("Enter the radius of the sphere: "))
    sphere = Sphere(radius)
    print(f"\nSphere with radius {radius}:")
    print(f"Volume: {sphere.volume()} cubic units")

elif choice == 4:
    # Cylinder
    radius = float(input("Enter the radius of the cylinder: "))
    height = float(input("Enter the height of the cylinder: "))
    cylinder = Cylinder(radius, height)
    print(f"\nCylinder with radius {radius} and height {height}:")
    print(f"Volume: {cylinder.volume()} cubic units")
    
    # Cone
    radius = float(input("\nEnter the radius of the cone: "))
    height = float(input("Enter the height of the cone: "))
    cone = Cone(radius, height)
    print(f"\nCone with radius {radius} and height {height}:")
    print(f"Volume: {cone.volume()} cubic units")
    
    # Sphere
    radius = float(input("\nEnter the radius of the sphere: "))
    sphere = Sphere(radius)
    print(f"\nSphere with radius {radius}:")
    print(f"Volume: {sphere.volume()} cubic units")
    
    # Demonstrating abstraction
    print("\n--- Demonstrating Abstraction ---")
    shapes = [cylinder, cone, sphere]
    shape_names = ["Cylinder", "Cone", "Sphere"]
    for name, shape in zip(shape_names, shapes):
        print(f"{name} Volume: {shape.volume()} cubic units")

else:
    print("Invalid choice!")
