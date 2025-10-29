import math

# Base Shape class
class Shape:
    def area(self):
        pass
    
    def perimeter(self):
        pass

# Circle subclass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

# Triangle subclass
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def area(self):
        # Using Heron's formula
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def perimeter(self):
        return self.a + self.b + self.c

# Square subclass
class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2
    
    def perimeter(self):
        return 4 * self.side

# Main program
print("Shape Calculator")
print("=" * 50)

# Circle
print("\n1. CIRCLE")
radius = float(input("Enter the radius of the circle: "))
circle = Circle(radius)
print(f"Area: {circle.area():.2f}")
print(f"Perimeter: {circle.perimeter():.2f}")

# Triangle
print("\n2. TRIANGLE")
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
triangle = Triangle(a, b, c)
print(f"Area: {triangle.area():.2f}")
print(f"Perimeter: {triangle.perimeter():.2f}")

# Square
print("\n3. SQUARE")
side = float(input("Enter the side of the square: "))
square = Square(side)
print(f"Area: {square.area():.2f}")
print(f"Perimeter: {square.perimeter():.2f}")
