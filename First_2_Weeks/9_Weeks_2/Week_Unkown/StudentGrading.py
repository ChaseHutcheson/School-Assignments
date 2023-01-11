student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for x, y in student_scores.items():
    if student_scores[x] >= 91:
        y = "Outstanding"
        student_grades.__setitem__(x, y)
    elif student_scores[x] >= 81:
        y = "Exceeds Expectations"
        student_grades.__setitem__(x, y)
    elif student_scores[x] >= 71:
        y = "Acceptable"
        student_grades.__setitem__(x, y)
    else:
        y = "Fail"
        student_grades.__setitem__(x, y)

print(student_grades)