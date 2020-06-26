# Else If Statements

# Calvin Coolidge’s Cool College has noticed that students prefer to get letter grades over GPA numbers. They want you to write a function called grade_converter that converts an inputted GPA into the appropriate letter grade. Your function should be named grade_converter, take the input gpa, and convert the following GPAs:
# 4.0 or higher should return "A"
# 3.0 or higher should return "B"
# 2.0 or higher should return "C"
# 1.0 or higher should return "D"
# 0.0 or higher should return "F"
# You can do this by creating a variable called grade.
# Then, you should use elif statements to set grade to the appropriate letter grade for the gpa entered.
# At the end of the function, return grade.
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