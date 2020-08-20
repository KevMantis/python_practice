# Quicksort Review

# Congratulations on implementing the quicksort algorithm in Python. To review:
# 1. We established a base case where the algorithm will complete when the start and end pointers indicate a list with one or zero elements
# 2. If we haven’t hit the base case, we randomly selected an element as the pivot and swapped it to the end of the list
# 3. We then iterate through that list and track all the “lesser than” elements by swapping them with the iteration index and incrementing a lesser_than_pointer.
# 4. Once we’ve iterated through the list, we swap the pivot element with the element located at lesser_than_pointer.
# 5. With the list partitioned into two sub-lists, we repeat the process on both halves until base cases are met.

# We’ve included the complete quicksort algorithm with some extra comments and print statements. Run the code to see a more detailed breakdown of each step!

from random import randrange, shuffle

def quicksort(list, start, end):
  # this portion of list has been sorted
  if start >= end:
    return
  print("Running quicksort on {0}".format(list[start: end + 1]))
  # select random element to be pivot
  pivot_idx = randrange(start, end + 1)
  pivot_element = list[pivot_idx]
  print("Selected pivot {0}".format(pivot_element))
  # swap random element with last element in sub-lists
  list[end], list[pivot_idx] = list[pivot_idx], list[end]

  # tracks all elements which should be to left (lesser than) pivot
  less_than_pointer = start
  
  for i in range(start, end):
    # we found an element out of place
    if list[i] < pivot_element:
      # swap element to the right-most portion of lesser elements
      print("Swapping {0} with {1}".format(list[i], pivot_element))
      list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
      # tally that we have one more lesser element
      less_than_pointer += 1
  # move pivot element to the right-most portion of lesser elements
  list[end], list[less_than_pointer] = list[less_than_pointer], list[end]
  print("{0} successfully partitioned".format(list[start: end + 1]))
  # recursively sort left and right sub-lists
  quicksort(list, start, less_than_pointer - 1)
  quicksort(list, less_than_pointer + 1, end)


    
  
list = [5,3,1,7,4,6,2,8]
shuffle(list)
print("PRE SORT: ", list)
print(quicksort(list, 0, len(list) -1))
print("POST SORT: ", list)
