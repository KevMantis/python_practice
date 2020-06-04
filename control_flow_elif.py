def grade_converter(gpa):
  if gpa >= 4.0:
    grade = "A"
  elif gpa >= 3.0:
    grade = "B"
  elif gpa >= 2.0:
    grade = "C"
  elif gpa >= 1.0:
    grade = "D"
  else:
    grade = "F"
  return grade

print(grade_converter(0.5))
