# Boolean Operators: not

# Set the variables statement_one and statement_two equal to the results of the following boolean expressions:
# Statement one:
# not (4 + 5 <= 9)
statement_one = False
# Statement two:
# not (8 * 2) != 20 - 4
statement_one = False

# The registrar’s office at Calvin Coolidge’s Cool College has been so impressed with your work so far that they have another task for you. They want you to return to the first function you wrote, graduation_reqs, and add in several checks using and and not statements.
# If a student meets both requirements the function should return
# "You meet the requirements to graduate!"
# If a student’s GPA is greater or equal to 2.0 but they don’t have enough credits the function should return
# "You do not have enough credits to graduate."
# If they have enough credits but their GPA is less than 2.0 the function should return
# "Your GPA is not high enough to graduate."
# If they do not have enough credits and their GPA is less than 2.0, the function should return
# "You do not meet either requirement to graduate!"
# Make sure your return value matches those strings exactly. Capitalization, punctuation, and spaces matter!
def graduation_reqs(gpa, credits):
  if (gpa >= 2.0) and (credits >= 120):
    return "You meet the requirements to graduate!"
  if (gpa >= 2.0) and (credits < 120):
    return "You do not have enough credits to graduate."
  if (gpa < 2.0) and (credits >= 120):
    return "Your GPA is not high enough to graduate."
  if (gpa < 2.0) and (credits < 120):
    return "You do not meet either requirement to graduate!"

print(graduation_reqs(1.9,120))