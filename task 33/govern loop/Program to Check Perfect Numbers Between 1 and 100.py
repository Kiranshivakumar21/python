def is_perfect(n):
    """Check if n is a perfect number."""
    if n < 2:
        return False
    divisor_sum = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisor_sum += i
            if i != n // i:
                divisor_sum += n // i
    return divisor_sum == n

num = int(input("Enter a number between 1 and 100: "))

if 1 <= num <= 100:
    if is_perfect(num):
        print(f"{num} is a perfect number.")
    else:
        print(f"{num} is not a perfect number.")
else:
    print("Number not in range 1 to 100.")
