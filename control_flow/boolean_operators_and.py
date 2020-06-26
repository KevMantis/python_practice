# Boolean Operators: and

# Set the variables statement_one and statement_two equal to the results of the following boolean expressions:
# Statement one:
# (2 + 2 + 2 >= 6) and (-1 * -1 < 0)
statement_one = False
# Statement two:
# (4 * 2 <= 8) and (7 - 1 == 6)
statement_two = True

# Let’s return to Calvin Coolidge’s Cool College. 120 credits aren’t the only graduation requirement, you also need to have a GPA of 2.0 or higher. Rewrite the graduation_reqs function so it takes two inputs, gpa and credits, and checks to see if a student meets both requirements using an and statement.
# If they do, return the string
# "You meet the requirements to graduate!"
def graduation_reqs(credits,gpa):
  if credits >= 120 and gpa >= 2.0:
    return "You meet the requirements to graduate!"

print(graduation_reqs(120,1.9))