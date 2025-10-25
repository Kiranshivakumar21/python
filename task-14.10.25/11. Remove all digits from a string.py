text = input("enter a alpha numeric sentence:")
result = ""

for char in text:
    if not char.isdigit():
        result = result + char

print(result)
