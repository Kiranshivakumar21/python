names = []
inputs = ["Alice", "Bob", "stop"]
for n in inputs:
    if n.lower() == "stop":
        break
    names.append(n)
print(names)
