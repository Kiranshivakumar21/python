def get_dict():
    d = {}
    n = int(input("How many items: "))
    for i in range(n):
        k = input("Key: ")
        v = int(input("Value: "))
        d[k] = v
    return d

def print_dict(d):
    print("Dictionary:", d)

def sum_dict(d):
    print("Sum of values:", sum(d.values()))
