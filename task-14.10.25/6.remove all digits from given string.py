text = "since 2001"
result = ""

for ch in text:
    if not ch.isdigit():
        result = result + ch
print(result)
