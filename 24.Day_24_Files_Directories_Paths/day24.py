# DAY 24

file = open('my_file.txt')
contents = file.read()
print(contents)

file.close()  # always close the file when done, since its using memory

with open('C:/Users/Bart/Desktop/my_file.txt') as file:
    # do this
    # does that
    pass
# python will close the file itself

# write - will make an empty file, or delete everything and do what you code
with open('../../my_file.txt', mode='w') as my_file:
    my_file.write('New text.')

# append - will open and add to an existing file at the every end, so usually use new line symbol
# or create empty file if it does not exist
with open('my_file.txt', mode='a') as my_file:
    my_file.write('\nOne two three, cha cha cha.')

# Challenge 1
# Save the high score from Snake Game into a txt file
# Read from txt file when opening the Snake Game

# Relative and Absolute File Paths

# absolute file paths start always at the root
# c\work\report.doc

# relative file paths
# from working directory, if we are in the folder \work, the relative file path to report.doc becomes \report.doc

# if the file is in the same working directory .\
# to go up the root we write ..
