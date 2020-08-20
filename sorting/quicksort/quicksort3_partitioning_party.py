# Partitioning Party

# We need to partition our list into two sub-lists of greater than or smaller than elements, and we’re going to do this “in-place” without creating new lists. Strap in, this is the most complex portion of the algorithm!
# Because we’re doing this in-place, we’ll need two pointers. One pointer will keep track of the “lesser than” elements. We can think of it as the border where all values at a lower index are lower in value to the pivot. The other pointer will track our progress through the list.
# Let’s explore how this will work in an example:
"""
[5, 6, 2, 3, 1, 4]
# we randomly select "3" and swap with the last element
[5, 6, 2, 4, 1, 3]

# We'll use () to mark our "lesser than" pointer
# We'll use {} to mark our progress through the list

[{(5)}, 6, 2, 4, 1, 3]
# {5} is not less than 3, so the "lesser than" pointer doesn't move

[(5), {6}, 2, 4, 1, 3]
# {6} is not less than 3, so the "lesser than" pointer doesn't move

[(5), 6, {2}, 4, 1, 3]
# {2} is less than 3, so we SWAP the values...
[(2), 6, {5}, 4, 1, 3]
# Then we increment the "lesser than" pointer
[2, (6), {5}, 4, 1, 3]

[2, (6), 5, {4}, 1, 3]
# {4} is not less than 3, so the "lesser than" pointer doesn't move

[2, (6), 5, 4, {1}, 3]
# {1} is less than 3, so we SWAP the values...
[2, (1), 5, 4, {6}, 3]
# Then we increment the "lesser than" pointer
[2, 1, (5), 4, {6}, 3]

# We've reached the end of the non-pivot values
[2, 1, (5), 4, 6, {3}]
# Swap the "lesser than" pointer with the pivot...
[2, 1, (3), 4, 6, {5}]
"""
# Tada! We have successfully partitioned this list. Note that the “sub-lists” are not necessarily sorted, we’ll need to recursively run the algorithm on each sub-list, but the pivot has arrived at the correct location within the list.

from random import randrange

def quicksort(list, start, end):
  if start >= end:
    return list

  pivot_idx = randrange(start, end)
  pivot_element = list[pivot_idx]
  list[end], list[pivot_idx] = list[pivot_idx], list[end]

  # Create the variable lesser_than_pointer and assign it to the start of the list.
  lesser_than_pointer = start
  
  # Create a for loop that iterates from start to end, and set the iterating variable to idx. This will track our progress through the list (or sub-list) we’re partitioning.
  # To start, write continue in the for loop.
  for idx in range(start, end):
    #continue
    # Within the loop, remove continue and replace it with a conditional.
    # We need to do something if the element at idx is less than pivot_element.
    # If so:
      # 1. Use parallel assignment to swap the values at lesser_than_pointer and idx.
      # 2. Increment the lesser_than_pointer
    if list[idx] < pivot_element:
      list[lesser_than_pointer], list[idx] = list[idx], list[lesser_than_pointer]
      lesser_than_pointer += 1
  
  # Once the loop concludes, use parallel assignment to swap the pivot element with the value located at lesser_than_pointer.
  # Here’s an example:
  """
  colors = ["blue", "red", "green"]
  colors[0], colors[1] = colors[1], colors[0]
  # ["red", "blue", "green"]
  """
  list[end], list[lesser_than_pointer] = list[lesser_than_pointer], list[end]

  print(list[start])
  start += 1
  return quicksort(list, start, end)

my_list = [42, 103, 22]
print("BEFORE: ", my_list)
sorted_list = quicksort(my_list, 0, len(my_list) - 1)
print("AFTER: ", sorted_list)