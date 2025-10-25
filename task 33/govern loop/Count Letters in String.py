def count_letters():
    string = input("Enter a string: ")
    letter_count = sum(1 for char in string if char.isalpha())
    print(f"Number of letters: {letter_count}")
    return letter_count
