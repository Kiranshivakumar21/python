square_dict = {x: x**2 for x in range(1, 16)}
keys_from_square = list(square_dict.keys())
new_dict_from_keys = {key: None for key in keys_from_square}
print(new_dict_from_keys)
