# Iterative Binary Search

# Anything recursive can be written iteratively.
# As a final exercise, we’ll implement the binary search algorithm using iteration.
# Our strategy remains largely the same as the recursive approach which used pointers.
# Instead of recursive calls, we’ll substitute a while loop.

# Complete the binary_search() skeleton.
# You’ll need to:
# - Fill in the condition for the while loop
# - Calculate the middle index using pointers
# - Set the left_pointer when appropriate
# - Set the right_pointer when appropriate

def binary_search(sorted_list, target):
  left_pointer = 0
  right_pointer = len(sorted_list)
  
  # fill in the condition for the while loop
  while left_pointer < right_pointer:
    # calculate the middle index using the two pointers
    mid_idx = (left_pointer + right_pointer) // 2
    mid_val = sorted_list[mid_idx]
    if mid_val == target:
      return mid_idx
    if target < mid_val:
      # set the right_pointer to the appropriate value
      right_pointer = mid_idx
    if target > mid_val:
      # set the left_pointer to the appropriate value
      left_pointer = mid_idx + 1
  
  return "Value not in list"

# test cases
print(binary_search([5,6,7,8,9], 9))
print(binary_search([5,6,7,8,9], 10))
print(binary_search([5,6,7,8,9], 8))
print(binary_search([5,6,7,8,9], 4))
print(binary_search([5,6,7,8,9], 6))