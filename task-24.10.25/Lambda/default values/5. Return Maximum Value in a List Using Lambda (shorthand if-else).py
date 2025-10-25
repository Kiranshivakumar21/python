nums = [10, 25, 37, 88, 100, 56, 89]
# Lambda for max of two numbers
max_lambda = lambda x, y: x if x > y else y
# Reduce to get maximum value
from functools import reduce
max_value = reduce(max_lambda, nums)
print("example numbers:", nums)
print("Maximum Value:", max_value)
