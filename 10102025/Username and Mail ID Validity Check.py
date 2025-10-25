import re

username = input("Enter username: ")
mail_id = input("Enter mail id: ")

if re.match("^[A-Za-z0-9_]{3,}$", username):
    print("Username is valid")
else:
    print("Username is NOT valid")

if re.match(r"[^@]+@[^@]+\.[^@]+", mail_id):
    print("Mail ID is valid")
else:
    print("Mail ID is NOT valid")
