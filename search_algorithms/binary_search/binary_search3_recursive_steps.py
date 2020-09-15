# Recursive Binary Search: The Recursive Steps

# With both of our base cases covered, we’ll turn our attention to the recursive step.
# We have two options depending on the comparison of mid_val to target.
# You’ll recall that our data-set is sorted.
# We’ll leverage that knowledge in our recursive step to cut the problem in half at each step.
# If the mid_val is greater than our target, we know we can disregard every element at an index greater than mid_idx:
"""
sorted_list = [9, 10, 11, 12, 13]
target = 9

mid_idx = len(sorted_list) // 2
# 2
mid_val = sorted_list[mid_idx]
# 11

11 > 9
# True
# No need to check right half: [12, 13]
# Those values will only be bigger...
# Instead, we'll check the left half!

left_half = sorted_list[:mid_idx]
# [9, 10]

# If mid_val had been less than the target
# We would check in the right half...

target = 17

17 > mid_val
right_half = sorted_list[mid_idx + 1:]
# [12, 13]
"""

def binary_search(sorted_list, target):
  if not sorted_list:
    return 'value not found'
  mid_idx = len(sorted_list)//2
  mid_val = sorted_list[mid_idx]
  if mid_val == target:
    return mid_idx
  # Below our check for whether mid_val == target make a new conditional.
  # Check whether the middle value is greater than the target.
  # If it is:
  # - make a variable: left_half that is every element in sorted_list up to but not including mid_val.
  # - return a recursive call to binary_search() given left_half and target as arguments.
  if mid_val > target:
    left_half = sorted_list[:mid_idx]
    return binary_search(left_half, target)
  # Make another conditional below the last checking if mid_val is less than our target.
  # If it is:
  # - make a variable: right_half that is every element in sorted_list after mid_val.
  # - make a variable: result and assign it to a recursive call of binary_search() given right_half and target.
  # Why are we storing this in a variable?
  # We’re making a smaller copy of the sorted list at each recursive call, so our indices for the same values change:
  """
  sorted_list = [7, 8, 9, 10, 11]
  right_half = [10, 11]

  # index of "11" in sorted_list: 4
  # index of "11" in right_half: 1
  """
  # We can account for the missing indices by returning the result plus the index segments of the lists we’ve discarded.
  # We’ll do this in the form of mid_idx + 1.
  """
  sorted_list = [7, 8, 9, 10, 11]
  binary_search(sorted_list, 11)
  mid_idx = 2
  # 9 < 11, we search in right half...
  # within the recursive call:
  # right_half = [10, 11]
  # mid_idx = 1
  # target matched, we return 1
  # within original call, result is 1
  (result + mid_idx + 1) == 4
  """
  # Return result plus the missing indices.
  if mid_val < target:
    right_half = sorted_list[mid_idx + 1:]
    result = binary_search(right_half, target)
    # When we search in the right half of the list and find the value, this works.
    # Unfortunately, there’s an error if we can’t locate the value: We’ll try to add "value not found" to mid_idx + 1, resulting in a TypeError.
    # Add in a conditional:
    # - If result is "value not found"
    #   - then return result.
    # Otherwise, return the index arithmetic as before.
    if result == "value not found":
      return result
    else:
      return result + mid_idx + 1

# For testing:
sorted_values = [13, 14, 15, 16, 17]
print(binary_search(sorted_values, 16))