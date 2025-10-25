def combination(n, r):
    fact = lambda x: 1 if x == 0 or x == 1 else x * fact(x-1)
    return fact(n) // (fact(r) * fact(n-r))
print(combination(5, 2))
