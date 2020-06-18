# Review - Username and Password Generator

# 1. Copeland’s Corporate Company has finalized what they want to their username and temporary password creation to be and have enlisted your help, once again, to build the function to generate them. In this exercise, you will create two functions, username_generator and password_generator.

# Let’s start with username_generator. Create a function called username_generator take two inputs, first_name and last_name and returns a username. The username should be a slice of the first three letters of their first name and the first four letters of their last name. If their first name is less than three letters or their last name is less than four letters it should use their entire names.

# For example, if the employee’s name is Abe Simpson the function should generate the username AbeSimp.

# 2. Great work! Now for the temporary password, they want the function to take the input user name and shift all of the letters by one to the right, so the last letter of the username ends up as the first letter and so forth. For example, if the username is AbeSimp, then the temporary password generated should be pAbeSim.

# Start by defining the function password_generator so that it takes one input, username and in it define an empty string named password.

# 3. Inside password_generator create a for loop that iterates through the indices username by going from 0 to len(username).

# To shift the letters right, at each letter the for loop should add the previous letter to the string password.

first_name = "Kevin"
last_name = "Green"

def username_generator(first_name, last_name):
  if len(first_name) <= 3 and len(last_name) > 4:
    return first_name + last_name[:4]
  elif len(first_name) > 3 and len(last_name) <= 4:
    return first_name[:3] + last_name
  else:
    return first_name[:3] + last_name[:4]

username = username_generator(first_name, last_name)

def password_generator(username):
  password = username[-1]
  for index in range(len(username) - 1):
    password = password + username[index]
  return password

password = password_generator(username)

print("User Name: " + username)
print("Password: " + password)
