count = 0
total = 0
for i in range(100, 201):
 if i % 9 == 0:
  count += 1
total += i
print("Count:", count)
print("Sum:", total)
