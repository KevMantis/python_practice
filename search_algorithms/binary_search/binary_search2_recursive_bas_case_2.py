# Recursive Binary Search: Base Case 2

# We now have a base case for when we do not find the value in our sorted list, but we need a base case for when we DO find the value.
# At this step, we have three options:
# - BASE CASE: mid_val matches our target
# - RECURSIVE STEP: mid_val is less than our target
# - RECURSIVE STEP: mid_val is more than our target
# We’ll tackle the alternate base case first.

def binary_search(sorted_list, target):
  if not sorted_list:
    return 'value not found'
  mid_idx = len(sorted_list)//2
  mid_val = sorted_list[mid_idx]
  # Let’s complete the base case for when we have found the value.
  # After the declarations for mid_val and mid_idx, write a conditional that checks if mid_val is our target.
  # If it is, return mid_idx.
  if mid_val == target:
    return mid_idx

# For testing:
sorted_values = [13, 14, 15, 16, 17]
print(binary_search([], 42))
print(binary_search(sorted_values, 42))
print(binary_search(sorted_values, 15))