num1 = float(input("Enter first value: "))
num2 = float(input("Enter second value: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == '+':
    print("Sum:", num1 + num2)
elif operation == '-':
    print("Difference:", num1 - num2)
elif operation == '*':
    print("Product:", num1 * num2)
elif operation == '/':
    if num2 != 0:
        print("Quotient:", num1 / num2)
    else:
        print("Division by zero is not allowed.")
else:
    print("Invalid operation selected.")
