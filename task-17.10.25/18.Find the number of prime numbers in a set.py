# Task 18: Find the number of prime numbers in a set
print("^" * 60)
print("Task 18: Find the number of prime numbers in a set")
print("^" * 60)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
print("Set of numbers:", numbers)

prime_numbers = {num for num in numbers if is_prime(num)}
print("Prime numbers:", prime_numbers)
print("Number of prime numbers:", len(prime_numbers))
print()

