# Greetings

# Create a function named add_greetings() which takes a list of strings named names as a parameter.

# In the function, create an empty list that will contain each greeting. Add the string "Hello, " in front of each name in names and append the greeting to the list.

# Return the new list containing the greetings.

def add_greetings(names):
  hello_name = []
  for name in names:
    hello_name.append('Hello, ' + name)
  return hello_name

print(add_greetings(["Owen", "Max", "Sophie"]))
