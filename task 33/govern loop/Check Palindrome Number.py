s = input("Enter a number: ")
print(f"{s} is", "a palindrome" if s==s[::-1] else "not a palindrome")
