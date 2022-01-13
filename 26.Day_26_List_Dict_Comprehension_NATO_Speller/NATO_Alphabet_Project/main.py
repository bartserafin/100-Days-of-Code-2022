# Crate a console program that takes string as input, and outputs a NATO spelled version of that input
# example:
# Input: 'Bart'
# Output: ['Bravo', 'Alfa', 'Romeo', 'Tango']


import pandas

# Create a NATO Dictionary
df = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}
# print(nato_dict)

# Create a list of code words for the input word
word = input('What is the word you want to spell? ').upper()
result = [nato_dict[char] for char in word]
print(result)


### FUNCTION ###


# def nato_speller(word2):
#
#     # Create a NATO Dictionary
#     df2 = pandas.read_csv('nato_phonetic_alphabet.csv')
#     nato_dict2 = {row.letter: row.code for (index, row) in df2.iterrows()}
#
#     # Create a list of code words for the input word
#     # word = input('What is the word you want to spell? ').upper()
#     word2 = word2.upper()
#     result2 = [nato_dict2[char] for char in word2]
#     return result2
#
#
# print(nato_speller('bart'))





