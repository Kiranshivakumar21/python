from abc import ABC, abstractmethod
import math

# Abstract class Shape
class Shape(ABC):
    @abstractmethod
    def calculateArea(self):
        """Abstract method to calculate area"""
        pass
    
    @abstractmethod
    def calculatePerimeter(self):
        """Abstract method to calculate perimeter"""
        pass

# Circle class inheriting from Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculateArea(self):
        area = math.pi * self.radius ** 2
        return round(area, 2)
    
    def calculatePerimeter(self):
        perimeter = 2 * math.pi * self.radius
        return round(perimeter, 2)

# Triangle class inheriting from Shape
class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def calculateArea(self):
        # Using Heron's formula
        s = (self.side1 + self.side2 + self.side3) / 2
        area = math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
        return round(area, 2)
    
    def calculatePerimeter(self):
        perimeter = self.side1 + self.side2 + self.side3
        return round(perimeter, 2)

# Main program
print("=== Abstract Class Shape Demo ===\n")

print("Choose a shape:")
print("1. Circle")
print("2. Triangle")
print("3. Both")

choice = int(input("\nEnter your choice (1-3): "))
print()

if choice == 1:
    radius = float(input("Enter the radius of the circle: "))
    circle = Circle(radius)
    print(f"\nCircle with radius {radius}:")
    print(f"Area: {circle.calculateArea()}")
    print(f"Perimeter (Circumference): {circle.calculatePerimeter()}")

elif choice == 2:
    print("Enter the three sides of the triangle:")
    side1 = float(input("Side 1: "))
    side2 = float(input("Side 2: "))
    side3 = float(input("Side 3: "))
    triangle = Triangle(side1, side2, side3)
    print(f"\nTriangle with sides {side1}, {side2}, {side3}:")
    print(f"Area: {triangle.calculateArea()}")
    print(f"Perimeter: {triangle.calculatePerimeter()}")

elif choice == 3:
    # Circle
    radius = float(input("Enter the radius of the circle: "))
    circle = Circle(radius)
    print(f"\nCircle with radius {radius}:")
    print(f"Area: {circle.calculateArea()}")
    print(f"Perimeter (Circumference): {circle.calculatePerimeter()}")
    
    # Triangle
    print("\nEnter the three sides of the triangle:")
    side1 = float(input("Side 1: "))
    side2 = float(input("Side 2: "))
    side3 = float(input("Side 3: "))
    triangle = Triangle(side1, side2, side3)
    print(f"\nTriangle with sides {side1}, {side2}, {side3}:")
    print(f"Area: {triangle.calculateArea()}")
    print(f"Perimeter: {triangle.calculatePerimeter()}")
    
    # Demonstrating abstraction
    print("\n--- Demonstrating Abstraction ---")
    shapes = [circle, triangle]
    for i, shape in enumerate(shapes, 1):
        print(f"\nShape {i}:")
        print(f"Area: {shape.calculateArea()}")
        print(f"Perimeter: {shape.calculatePerimeter()}")

else:
    print("Invalid choice!")
