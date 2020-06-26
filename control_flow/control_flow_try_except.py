# Try and Except Statements

# The function in the editor is very simple and serves one purpose: it raises a ValueError.
# Try running it by entering raises_value_error() into the code editor and hitting run.
# Remember, unindent this function call so it isn’t included in the function itself.
def raises_value_error():
  raise ValueError

# Great! Nice error raising! Now let’s make that error message a little more palatable.
# Write a try statement and an except statement around the line of code that executes the function to catch a ValueError and make the error message print You raised a ValueError!
try:
  raises_value_error()
except ValueError:
  print("You raised a ValueError!")