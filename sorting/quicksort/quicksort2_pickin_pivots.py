# Pickin' Pivots

# Quicksort works by selecting a pivot element and dividing the list into two sub-lists of values greater than or less than the pivot element’s value. This process of “partitioning” the list breaks the problem down into two smaller sub-lists.
# For the algorithm to remain efficient, those sub-lists should be close to equal in length. Here’s an example:
"""
[9, 3, 21, 4, 50, 8, 11]
# pick the first element, 9, as the pivot
# "lesser_than_list" becomes [3, 4, 8]
# "greater_than_list" becomes [21, 50, 11]
"""
# In this example the two sub-lists are equal in length, but what happens if we pick the first element as a pivot in a sorted list?
"""
[1, 2, 3, 4, 5, 6]
# pick the first element, 1, as the pivot
# "lesser_than_list" becomes []
# "greater_than_list" becomes [2,3,4,5,6]
"""
# Our partition step has produced severely unbalanced sub-lists! While it may seem silly to sort an already sorted list, this is a common enough occurrence that we’ll need to make an adjustment.
# We can avoid this problem by randomly selecting a pivot element from the list each time we partition. The benefit of random selection is that no particular data set will consistently cause trouble for the algorithm! We’ll then swap this random element with the last element of the list so our code consistently knows where to find the pivot.

from random import randrange

def quicksort(list, start, end):
  if start >= end:
    return list
	# We’ve imported the randrange() function to assist with the random pivot. Check the documentation for how it works. https://docs.python.org/3/library/random.html#random.randrange
  # Use this function to create the variable pivot_idx, a random index between start and end.
  pivot_idx = randrange(start, end)
  # Make another variable pivot_element and use pivot_idx to retrieve the value located in the list which was passed in as an argument.
  pivot_element = list[pivot_idx]
  # Random is great because it protects our algorithm against inefficient runtimes, but our code will be simpler for the remainder of the algorithm if we know the pivot will always be in the same place.
  # Swap the end element of the list with the pivot_idx so we know the pivot element will always be located at the end of the list.
  list[end], list[pivot_idx] = list[pivot_idx], list[end]

  # Leave these lines for testing
  print(list[start])
  start += 1
  return quicksort(list, start, end)

my_list = [32, 22]
print("BEFORE: ", my_list)
sorted_list = quicksort(my_list, 0, len(my_list) - 1)
print("AFTER: ", sorted_list)