# Pattern 1: Left-Aligned Increasing Numbers
print("Pattern 1:")
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=' ')
    print()
print()

# Pattern 2: Left-Aligned Decreasing Numbers
print("Pattern 2:")
for i in range(5, 0, -1):
    for j in range(1, i+1):
        print(j, end=' ')
    print()
print()

# Pattern 3: Right-Aligned Decreasing Numbers
print("Pattern 3:")
rows = 6
for i in range(1, rows + 1):
    if i == 1 or i == rows:
        print('*' * i)
    else:
        print('*' + ' ' * (i - 2) + '*')
    print()
print()

# Pattern 4: Increasing Letters on Each Row
print("Pattern 4:")
for i in range(1, 7):
    print(chr(64+i) * i)
print()

# Pattern 5: Rectangle of Increasing Sequence of Letters (Grouped rows)
print("Pattern 5:")
n = 1
for i in range(1, 6):
    for j in range(i):
        print(chr(64 + n), end='')
        n += 1
    print()
print()

# Pattern 6: Square of Grouped Letters
print("Pattern 6:")
for i in range(1, 6):
    print(chr(64 + i) * i)
print()

# Pattern 7: Increasing Sequence of Letters per Row
print("Pattern 7:")
for i in range(1, 6):
    for j in range(1, i+1):
        print(chr(64 + j), end='')
    print()
