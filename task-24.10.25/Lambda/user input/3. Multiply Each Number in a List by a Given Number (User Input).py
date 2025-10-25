import math
nums = list(map(int, input("Enter numbers separated by space: ").split()))
n = int(input("Enter the multiplier: "))
result = list(map(lambda num: math.prod([num, n]), nums))
print("Multiplied List:", result)

