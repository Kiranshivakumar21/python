lst = ["a", "b", "c", "d"]
item_to_remove = input("Enter item to remove: ")
if item_to_remove in lst:
    lst.remove(item_to_remove)
else:
    print(f"{item_to_remove} not found in list.")
print(lst)
