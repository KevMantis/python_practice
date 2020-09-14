# Using Linear Search

# In the text editor, you will find the code for the linear_search() function that we implemented in Python.
# When called, our function returns either an index of an element that matches the target value or a ValueError express that the value was not found.
# The text editor includes the code for the linear_search() function, a list of numbers called number_list and a variable called target_number, which stores target value that we will be searching for in number_list.
# Let’s practice calling linear_search() and explore the return values for different calls to the function.

number_list = [ 10, 14, 19, 26, 27, 31, 33, 35, 42, 44]
target_number = 100 #33

def linear_search(search_list, target_value):
  for idx in range(len(search_list)):
    if search_list[idx] == target_value:
      return idx
  raise ValueError("{0} not in list".format(target_value))



try:
  # We’re searching for 33.
  # Call linear_search() to find whether the target_number is in number_list and set this to the variable result.
  # Print result.
  result = linear_search(number_list, target_number)
  print(result)

except ValueError as error_message:
  print("{0}".format(error_message))

# We won’t always find what we’re looking for.
# Within the try block provided, search for 100 to see what happens when a value is not found in the list.