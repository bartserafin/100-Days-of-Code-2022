#  List Comprehension
#  Unique for Python language



# so far we would make a new list form an existing list like so
numbers = [1, 2, 3]
new_numbers = []

for number in numbers:
    number += 1
    new_numbers.append(number)
print(new_numbers)

#  new_list = [new_item for item in list]

new_nums = [number + 1 for number in numbers]
print(new_nums)

# works with strings

name = 'Bartosz'
letters = [letter for letter in name]
print(letters)


# comprehension works with all Python Sequences
# that is list, range, string, tuple

in_a_row = [number * 2 for number in range(1, 5)]
print(in_a_row)


# conditional list comprehension
# we can add and if statement when the el should be added to a list

new_list = [number for number in range(1,10) if number % 3 == 0]
print(new_list)



###### Dictionary Comprehension #####

# new_dict = {new_key:new_value for (key,value) in dict.items()}

import random

students = ['Alex', 'Beth', 'Caroline', 'Dave']

scores = {student: random.randint(0, 100) for student in students}
print(scores)

passed_students = {student: score for (student, score) in scores.items() if score >= 60}
print(passed_students)


sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

result = {word: len(word) for word in sentence.split()}

print(result)


student_dict = {
    'student' : ["Angela", "James", "Lilly"],
    'score' : [56, 76, 98]
}

for (key, value) in student_dict.items():
    print(key, value)

import pandas

students_data_frame = pandas.DataFrame(student_dict)
print(students_data_frame)

# Loop through a data frame
# for (key, value) in students_data_frame.items():
#     print(key, value)

# pandas has in-built method for looping through the data frame
# loop through each row
for (index, row) in students_data_frame.iterrows():
    print(index)
    print(row)
    # print(row.student)
    # print(row.score)

    # if row.student == 'Angela':
    #     print(row.score)