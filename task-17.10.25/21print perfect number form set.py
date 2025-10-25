# Task 21: Print the perfect number from set
print("_" * 60)
print("Task 21: Print the perfect number from set")
print("*" * 60)

def is_perfect(n):
    if n < 2:
        return False
    divisor_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisor_sum += i
    return divisor_sum == n

numbers = {6, 12, 28, 30, 496, 100, 8128, 50}
print("Set of numbers:", numbers)

perfect_numbers = {num for num in numbers if is_perfect(num)}
print("Perfect numbers:", perfect_numbers)

# Show why they are perfect
for num in sorted(perfect_numbers):
    divisors = [i for i in range(1, num) if num % i == 0]
    print(f"{num} is perfect: divisors = {divisors}, sum = {sum(divisors)}")
print()

