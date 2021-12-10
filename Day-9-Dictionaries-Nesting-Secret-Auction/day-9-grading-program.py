student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}


# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for name, score in student_scores.items():
    if score <= 70:
        score = "Fail"
    elif 70 < score <= 80:
        score = "Acceptable"
    elif 80 < score <= 90:
        score = "Exceeds Expectations"
    elif 90 < score <= 100:
        score = "Outstanding"
    else:
        score = "Cheating"
    student_grades[name] = score

print(student_grades)