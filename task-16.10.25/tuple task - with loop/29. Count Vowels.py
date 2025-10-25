letters = ('a', 'b', 'e', 'i', 'o', 'u', 'x')
vowels = "aeiou"
count = 0
for ch in letters:
    if ch in vowels:
        count += 1
print("Vowel count:", count)
