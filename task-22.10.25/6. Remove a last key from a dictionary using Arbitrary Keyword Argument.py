def remove_last_key(**kwargs):
    dictionary = kwargs.get('dictionary', {})
    if dictionary:
        last_key = list(dictionary.keys())[-1]
        dictionary.pop(last_key)
    return dictionary

# Example
result = remove_last_key(dictionary={'a': 1, 'b': 2, 'c': 3})
print("After removing last key:", result)
