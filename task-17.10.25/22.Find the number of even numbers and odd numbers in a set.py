# Task 22: Find the number of even numbers and odd numbers in a set
print("<>" * 25)
print("Task 22: Find number of even & odd numbers in a set")
print("<>" * 25)

numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
print("Set of numbers:", numbers)

even_numbers = {num for num in numbers if num % 2 == 0}
odd_numbers = {num for num in numbers if num % 2 != 0}

print("\nEven numbers:", even_numbers)
print("Number of even numbers:", len(even_numbers))

print("\nOdd numbers:", odd_numbers)
print("Number of odd numbers:", len(odd_numbers))
