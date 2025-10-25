from functools import reduce
nums = list(map(int, input("Enter numbers separated by space: ").split()))
max_lambda = lambda x, y: x if x > y else y
max_value = reduce(max_lambda, nums)
print("Maximum Value:", max_value)
