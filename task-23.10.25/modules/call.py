#task 1
from logical import prime , perfect , armstrong
print("<>" * 25)
print("Task 1: logical.py")
print("<>" * 25)

a = int(input("Enter a number: "))
print(prime(7))        # Output: True
print(perfect(34567))     # Output: True
print(armstrong(153))  # Output: True

#task 2
from pattern import rightriangle , lefttriangle , inverserightriangle , inverselefttriangle
print("*" * 25)
print("Task 2: pattern.py")
print("*" * 25)

n = int(input("Enter rows: "))
print(rightriangle(n))
print(" " *25)
print(lefttriangle(n))
print(" " *25)
print(inverserightriangle(n))
print(" " *25)
print(inverselefttriangle(n))

#task 3
import dictionary  
print("*" * 25)
print("Task 3: dictionary.py")
print("*" * 25)


d = dictionary.get_dict()
dictionary.print_dict(d)
dictionary.sum_dict(d)
#print(f"Sum of values: {total}")

#task 4
from lst import get_list_values , print_list_values , count_even
print("-*-" * 15)
print("Task 4: list.py")
print("-*-" * 15)

lst = [1, 2, 3, 4, 6, 7, 8, 10]
print(get_list_values(lst))   # Output: [1, 2, 3, 4, 6, 7, 8, 10]
print(print_list_values(lst)) # Output: 1 2 3 4 6 7 8 10
print(count_even(lst))        # Output: 5



