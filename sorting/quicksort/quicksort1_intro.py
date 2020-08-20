# Quicksort Introduction

# We’ll be implementing a version of the quicksort algorithm in Python. Quicksort is an efficient way of sorting a list of values by partitioning the list into smaller sub-lists based on comparisons with a single “pivot” element.
# Our algorithm will be recursive, so we’ll have a base case and an inductive step that takes us closer to the base case. We’ll also sort our list in-place to keep it as efficient as possible.
# Sorting in place means we’ll need to keep track of the sub-lists in our algorithm using pointers and swap values inside the list rather than create new lists.
# We’ll use pointers a lot in this algorithm so it’s worth spending a little time practicing. Pointers are indices that keep track of a portion of a list. Here’s an example of using pointers to represent the entire list:
"""
my_list = ['pizza', 'burrito', 'sandwich', 'salad', 'noodles']
start_of_list = 0
end_of_list = len(my_list) - 1

my_list[start_of_list : end_of_list + 1]
# ['pizza', 'burrito', 'sandwich', 'salad', 'noodles']
"""
# Now, what if we wanted to keep my_list the same, but make a sub-list of only the first half?
"""
end_of_half_sub_list = len(my_list) // 2
# 2

my_list[start_of_list : end_of_half_sub_list + 1]
# ['pizza', 'burrito', 'sandwich']
"""
# Finally, let’s make a sub-list that excludes the first and last elements…
"""
start_of_sub_list = 1
end_of_sub_list = len(my_list) - 2

my_list[start_of_sub_list : end_of_sub_list]
# ['burrito', 'sandwich', 'salad']
"""
# Nice work! We’ll use two pointers, start and end to keep track of sub-lists in our algorithm. Let’s get started!

colors = ["blue", "red", "green", "purple", "orange"]

# In qs.py, define our quicksort function with list, start, and end as parameters.
# Write pass in the body of the function to start.
def quicksort(list, start, end):
  #pass
  # Replace the pass statement with a base case.
  # We’re going to be passing in the same list as an argument for each recursive call, but start and end will mark what part of the list we’re considering.
  # Our base case is when the list from start to end contains one or zero elements.
  """
  ["race cars", "lasers", "airplanes"]

  start = 1
  end = 1
  # start == end
  # A sub-list starting at index 1 and concluding at index 1 
  # ["lasers"]

  start = 2
  end = 1
  # start > end
  # A sub-list start index 2 and concluding at index 1
  # []
  """
  # If the base case is met, then return from the function.
  if start >= end:
    return
  # Let’s start with a simple inductive step which takes us closer to the base case we’ve just defined.
  # After the if statement, print out the element at start.
  # Then, increment start by one and recursively call quicksort with list, start, and end.
  # Test it out by calling quicksort on the colors list. You should see each color except the last printed out.
  print(list[start])
  start += 1
  return quicksort(list, start, end)

quicksort(colors, 0, 4)