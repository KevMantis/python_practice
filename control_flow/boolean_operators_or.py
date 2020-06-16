def graduation_mailer(gpa,credits):
  if gpa >= 2.0 or credits >= 120:
    return True

print(graduation_mailer(1.9,120))
