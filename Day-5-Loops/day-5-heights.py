student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

number_of_students = 0
for student in student_heights:
    number_of_students += 1

sum_heights = 0
for height in student_heights:
    sum_heights += height

avg = round(sum_heights / number_of_students)
print(avg)
