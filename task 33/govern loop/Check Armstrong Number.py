n = input("Enter a number: ")
power = len(n)
total = sum(int(d)**power for d in n)
print(f"{n} is", "an Armstrong number" if total==int(n) else "not an Armstrong number")
