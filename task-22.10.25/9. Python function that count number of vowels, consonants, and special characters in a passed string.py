def count_vowels_consonants_special(string):
    vowels = consonants = special = 0
    for char in string.lower():
        if char.isalpha():
            if char in 'aeiou':
                vowels += 1
            else:
                consonants += 1
        elif not char.isspace():
            special += 1
    return vowels, consonants, special

# Example
string = "Hello, World!"
v, c, s = count_vowels_consonants_special(string)
print("Vowels:", v, "Consonants:", c, "Special Characters:", s)
