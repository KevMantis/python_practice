# Boolean Operators: or

# Set the variables statement_one and statement_two equal to the results of the following boolean expressions:
# Statement one:
# (2 - 1 > 3) or (-5 * 2 == -10)
statement_one = True
# Statement two:
# (9 + 5 <= 15) or (7 != 4 + 3)
statement_two = True

# The registrars office at Calvin Coolidge’s Cool College has another request. They want to send out a mailer with information on the commencement ceremonies to students who have met at least one requirement for graduation (120 credits and 2.0 GPA).
# Write a function called graduation_mailer that takes two inputs, gpa and credits and checks if a student either has 120 or more credits or a GPA 2.0 or higher and if so returns True.
def graduation_mailer(gpa,credits):
  if gpa >= 2.0 or credits >= 120:
    return True

print(graduation_mailer(1.9,120))