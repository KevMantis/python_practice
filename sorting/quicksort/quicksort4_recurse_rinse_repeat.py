# Recurse, Rinse, Repeat

# We’ve made it through the trickiest portion of the algorithm, but we’re not quite finished. We’ve partitioned the list once, but we need to continue partitioning until the base case is met.
# Let’s revisit our example from the previous exercise where we had finished a single partition step:
"""
# the pivot, 3, is correctly placed
whole_list = [2, 1, (3), 4, 6, 5]

less_than_pointer = 2
start = 0
end = len(whole_list) - 1
# start and end are pointers encompassing the entire list
# pointers for the "lesser than" sub-list
left_sub_list_start = start
left_sub_list_end = less_than_pointer - 1

lesser_than_sub_list = whole_list[left_sub_list_start : left_sub_list_end]
# [2, 1]

# pointers for the "greater than" sub-list
right_sub_list_start = less_than_pointer + 1
right_sub_list_end = end
greater_than_sub_list = whole_list[right_sub_list_start : right_sub_list_end]
# [4, 6, 5]
"""
# The key insight is that we’ll recursively call quicksort and pass along these updated pointers to mark the various sub-lists. Make sure you’re excluding the index that stores the newly placed pivot value or we’ll never hit the base case!

from random import randrange, shuffle 
def quicksort(list, start, end):
  # this portion of listay has been sorted
  if start >= end:
    return

  # select random element to be pivot
  pivot_idx = randrange(start, end + 1)
  pivot_element = list[pivot_idx]

  # swap random element with last element in sub-listay
  list[end], list[pivot_idx] = list[pivot_idx], list[end]

  # tracks all elements which should be to left (lesser than) pivot
  less_than_pointer = start
  
  for i in range(start, end):
    # we found an element out of place
    if list[i] < pivot_element:
      # swap element to the right-most portion of lesser elements
      list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
      # tally that we have one more lesser element
      less_than_pointer += 1
  # move pivot element to the right-most portion of lesser elements
  list[end], list[less_than_pointer] = list[less_than_pointer], list[end]
  
  # Complete our quicksort algorithm by recursively calling quicksort on the left and right sub-lists.
  quicksort(list, start, less_than_pointer - 1)
  quicksort(list, less_than_pointer + 1, end)
  
  
unsorted_list = [3,7,12,24,36,42]
shuffle(unsorted_list)
print(unsorted_list)

# Call quicksort() on unsorted_list. Be sure to pass in all three arguments!
# Print unsorted_list.
quicksort(unsorted_list, 0, len(unsorted_list) - 1)
print(unsorted_list)