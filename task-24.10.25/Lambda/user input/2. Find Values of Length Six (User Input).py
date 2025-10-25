# Get user list input as space-separated strings
user_input = input("Enter words separated by space: ")
words = user_input.split()
length_six = list(filter(lambda w: len(w) == 6, words))
print("Words of length 6:", length_six)
