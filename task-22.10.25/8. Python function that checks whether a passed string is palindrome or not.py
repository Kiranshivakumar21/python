def is_palindrome(string):
    return string == string[::-1]

# Example
word = "madam"
print(f"{word} is palindrome:", is_palindrome(word))
