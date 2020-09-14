# Review

# You are a linear search whiz!
# You have implemented linear search as a function in Python and used it to find a target value, duplicates, and the largest value in different search lists.
# Let’s review what we learned:
# Linear search is a search algorithm that sequentially checks whether a given value is an element of specified list by scanning the elements of a list one-by-one until it finds the target value.
# Starting with linear search as a subroutine in your code is a useful foundation for constructing algorithms to solve more advanced search problems, such as:
# - Finding duplicates - sequentially search the list for all occurrences of the target value.
# - Finding the maximum value - sequentially scan the list for the largest value and track the largest value seen to date.
# The linear_search() function is provided in the text editor.
# Test on your own examples!

# A list of the ingredients for tuna sushi
recipe = ["nori", "tuna", "soy sauce", "sushi rice"]
target_ingredient = "avocado"

def linear_search(search_list, target_value):
  for idx in range(len(search_list)):
    if search_list[idx] == target_value:
      return idx
  raise ValueError("{0} not in list".format(target_value))

print(linear_search(recipe, target_ingredient))