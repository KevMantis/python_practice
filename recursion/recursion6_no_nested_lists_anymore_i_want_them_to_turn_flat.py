# No Nested Lists Anymore, I Want Them to Turn Flat

# Let’s use recursion to solve another problem involving lists: flatten().
# We want to write a function that removes nested lists within a list but keeps the values contained.
"""
nested_planets = ['mercury', 'venus', ['earth'], 'mars', [['jupiter', 'saturn']], 'uranus', ['neptune', 'pluto']]

flatten(nested_planets)
# ['mercury', 
#  'venus', 
#  'earth', 
#  'mars', 
#  'jupiter', 
#  'saturn', 
#  'uranus', 
#  'neptune', 
#  'pluto']
"""
# Remember our tools for recursive functions. We want to identify a base case, and we need to think about a recursive step that takes us closer to achieving the base case.
# For this problem, we have two scenarios as we move through the list.
# - The element in the list is a list itself.
#   - We have more work to do!
# - The element in the list is not a list.
#   - All set!
# Which is the base case and which is the recursive step?

# Define flatten() which has a single parameter named my_list.
# We’ll start by declaring a variable, result and setting it to an empty list.
# result is our intermediary variable that houses elements from my_list.
# Return result.
def flatten(my_list):
  result = []
  # Returning an empty list isn’t much good to us, it should be filled with the values contained in my_list.
  # Use a for loop to iterate through my_list.
  # Inside the loop, we need a conditional for our recursive step. Check if the element in the current iteration is a list.
  # We can use Python’s isinstance() like so:
  """
  a_list = ['listing it up!']
  not_a_list = 'string here'

  isinstance(a_list, list)
  # True
  isinstance(not_a_list, list)
  # False
  """
  # For now, print "List found!" in the conditional.
  # Outside of the method definition, call flatten() and pass planets as an argument.
  for element in my_list:
    if isinstance(element, list):
      print('List found!')
      # We need to make the recursive step draw us closer to the base case, where every element is not a list.
      # After your print statement, declare the variable flat_list, and assign it to a recursive call to flatten() passing in your iterating variable as the argument.
      # flatten() will return a list, update result so it now includes every element contained in flat_list.
      # Test flatten() by calling it on the planets and printing the result.
      flat_list = flatten(element)
      result += flat_list
      # Nice work! Now the base case.
      # If the iterating variable is not a list, we can update result, so it includes this element at the end of the list.
      # flatten() should now return the complete result.
      # Print the result!
    else:
      result.append(element)
  return result

### reserve for testing...
planets = ['mercury', 'venus', ['earth'], 'mars', [['jupiter', 'saturn']], 'uranus', ['neptune', 'pluto']]

print(flatten(planets))