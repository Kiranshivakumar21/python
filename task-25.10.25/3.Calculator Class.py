class Calculator:
    def add(self, a, b):
        return a + b
    
    def sub(self, a, b):
        return a - b
    
    def mul(self, a, b):
        return a * b
    
    def div(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"

# Get user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Create calculator object and perform operations
calc = Calculator()
print(f"\nCalculator Results:")
print(f"Addition: {num1} + {num2} = {calc.add(num1, num2)}")
print(f"Subtraction: {num1} - {num2} = {calc.sub(num1, num2)}")
print(f"Multiplication: {num1} * {num2} = {calc.mul(num1, num2)}")
print(f"Division: {num1} / {num2} = {calc.div(num1, num2)}")
