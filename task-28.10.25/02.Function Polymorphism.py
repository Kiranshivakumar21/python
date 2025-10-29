# Function Polymorphism
print("=== Function Polymorphism Demo ===\n")

def add(a, b, c=None):
    """Polymorphic function that can add 2 or 3 values of different types"""
    if c is None:
        return a + b
    else:
        return a + b + c

# Get user choice
print("Choose operation type:")
print("1. Add two integers")
print("2. Add three integers")
print("3. Concatenate two strings")
print("4. Concatenate three strings")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = add(num1, num2)
    print(f"\nResult: {num1} + {num2} = {result}")

elif choice == 2:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num3 = int(input("Enter third number: "))
    result = add(num1, num2, num3)
    print(f"\nResult: {num1} + {num2} + {num3} = {result}")

elif choice == 3:
    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")
    result = add(str1, str2)
    print(f"\nResult: '{str1}' + '{str2}' = '{result}'")

elif choice == 4:
    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")
    str3 = input("Enter third string: ")
    result = add(str1, str2, str3)
    print(f"\nResult: '{str1}' + '{str2}' + '{str3}' = '{result}'")

else:
    print("Invalid choice!")
