words = ['level', 'world', 'madam', 'python', 'noon', 'hello']
# Check palindrome using shorthand if-else
is_palindrome = list(map(lambda s: True if s == s[::-1] else False, words))
print("Palindrome example words:", words)
print("Palindrome status:", is_palindrome)
