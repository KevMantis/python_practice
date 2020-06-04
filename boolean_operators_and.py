statement_one = False

statement_two = True

def graduation_reqs(credits,gpa):
  if credits >= 120 and gpa >= 2.0:
    return "You meet the requirements to graduate!"

print(graduation_reqs(120,1.9))
