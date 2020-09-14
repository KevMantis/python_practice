# Implement Linear Search

# Linear search is used to search for a target value in a list. We examine each of the elements in the list and compare them with the target value until matching the target.
# If a match is found, the linear search function will return the index of the matching element. Otherwise, the function will raise a ValueError, a special error to indicate that the value was not found.
# Here is the pseudocode for linear search as a function:
"""
# For each element in the search_list
    # if element equal target value then
       # return its index
# if element is not found then 
    # raise a ValueError
"""
# Let’s convert the pseudocode into Python.

# Declare a function called linear_search() in Python with two parameters: search_list, as its first parameter, and target_value, as its second parameter.
# For now, in the body of your function, linear_search(), use the pass keyword.
# pass is a placeholder in areas of your code where Python expects an expression.

def linear_search(search_list, target_value):
  #pass
  # In the function linear_search():
  # Remove the pass keyword.
  # Create a for loop that iterates over the list using the range() and len() methods.
  # use the iterating variable to print each element in search_list
  # Uncomment the test code!
  for i in range(len(search_list)):
    print(search_list[i])
    # Within the for loop after printing the element:
    # Use an if statement that checks whether the element matches target_value.
    # If so, return the index.
    if search_list[i] == target_value:
      return i
  # If we complete the loop and there is not a match, use ValueError() to raise an exception.
  # Add a line outside the loop invoking raise ValueError() with "{target_value} not in list".
  # Interpolate target_value into the string, so if you’re searching for "biscuits" it reads: "biscuits not in list".
  raise ValueError("{} not in list".format(target_value))

values = [54, 22, 46, 99]
print(linear_search(values, 22))