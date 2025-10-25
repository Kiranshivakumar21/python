#Task 20: Find the number of vowels in each name in a set
print("_" * 60)
print("Task 20: Find the number of vowels in each name in a set")
print("^" * 60)

def count_vowels(name):
    vowels = "aeiouAEIOU"
    count = 0
    for char in name:
        if char in vowels:
            count += 1
    return count

names = {"Kumar", "Kunal", "Rahul", "Priya", "Ankit", "Ravi"}
print("Set of names:", names)
print("\nVowel count in each name:")
for name in sorted(names):
    vowel_count = count_vowels(name)
    print(f"{name}: {vowel_count} vowels")
print()
