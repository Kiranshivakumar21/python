def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

n = 10  # Example: first 10 terms
fib_sequence = fibonacci(n)
print(f"First {n} terms of Fibonacci series:", fib_sequence)
