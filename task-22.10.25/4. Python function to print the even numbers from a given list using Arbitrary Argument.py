def print_even_numbers(*args):
    evens = [num for num in args if num % 2 == 0]
    return evens

# Example
result = print_even_numbers(1, 2, 3, 4, 5, 6)
print("Even Numbers:", result)
