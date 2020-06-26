# Else Statements

# Calvin Coolidge’s Cool College has another request for you. They want you to add an additional check to the graduation_reqs function. If a student is failing to meet both graduation requirements, they want the function to return:
# "You do not meet the GPA or the credit requirement for graduation."
# Use an else statement to add this to your function.
def graduation_reqs(gpa, credits):
  if (gpa >= 2.0) and (credits >= 120):
    return "You meet the requirements to graduate!"
  if (gpa >= 2.0) and not (credits >= 120):
    return "You do not have enough credits to graduate."
  if not (gpa >= 2.0) and (credits >= 120):
    return "Your GPA is not high enough to graduate."
  else:
    return "You do not meet the GPA or the credit requirement for graduation."

print (graduation_reqs(1.9,119))