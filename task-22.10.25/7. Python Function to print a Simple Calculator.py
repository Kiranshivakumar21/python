def simple_calculator(a, b, operation):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b != 0:
            return a / b
        else:
            return "Division by zero error"
    else:
        return "Invalid operation"

# Example
print("Add:", simple_calculator(10, 5, 'add'))
print("Subtract:", simple_calculator(10, 5, 'subtract'))
print("Multiply:", simple_calculator(10, 5, 'multiply'))
print("Divide:", simple_calculator(10, 5, 'divide'))
