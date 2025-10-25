series = range(1, 21)
even = int (input ("enter a even number:"))
odd = int (input ("enter a odd number:"))
for i in series:
 if i % 2 == 0:
  even += 1
 else:
  odd += 1
print("Even numbers:", even)
print("Odd numbers:", odd)
