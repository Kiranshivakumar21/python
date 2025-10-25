# Given list
words = ['Python', 'Lambda', 'Always', 'Coding', 'Output', 'Script']
# Filter words with length 6
length_six = list(filter(lambda w: len(w) == 6, words))
print("Words of length 6:", length_six)
