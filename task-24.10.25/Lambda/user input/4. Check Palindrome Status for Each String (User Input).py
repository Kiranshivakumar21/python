words = input("Enter strings separated by space: ").split()
is_palindrome = list(map(lambda s: True if s == s[::-1] else False, words))
print("Palindrome status:", is_palindrome)
