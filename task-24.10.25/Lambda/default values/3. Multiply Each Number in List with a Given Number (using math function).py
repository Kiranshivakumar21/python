import math
nums = [2, 4, 6, 9, 11]
n = 3
# Multiply each number using lambda and map
result = list(map(lambda num: math.prod([num, n]), nums))
print("Multiplied List:", result)
