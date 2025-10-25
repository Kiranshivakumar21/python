def is_armstrong(n):
    """Check if n is an Armstrong number."""
    num_str = str(n)
    power = len(num_str)
    total = sum(int(digit) ** power for digit in num_str)
    return total == n

num = int(input("Enter a number between 1 and 1000: "))

if 1 <= num <= 1000:
    if is_armstrong(num):
        print(f"{num} is an Armstrong number.")
    else:
        print(f"{num} is not an Armstrong number.")
else:
    print("Number not in range 1 to 1000.")
