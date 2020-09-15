# Recursive Binary Search: Base Case

# Binary search is an efficient algorithm for finding values in a sorted data-set.
# Let’s implement this algorithm in Python!
# Here’s a recap of the algorithm:
# - Check the middle value of the dataset.
#   - If this value matches our target we return the target value index.
# - If the middle value is greater than our target
#   - Begin at step 1 using the left half of the list.
# - If the middle value is less than our target
#   - Begin at step 1 using the right half of the list.
# As an added challenge, we are going to use a recursive approach. When using recursion, we always want to think of the problem in two ways: the base case and the recursive step.
# We have two base cases for this algorithm:
# - We found the value and return its index
# - We didn’t find the value because the list is empty!
# In order to reach the base case of an empty list, we’ll need to remove an element at each recursive call…

# Define binary_search() which has two parameters: sorted_list and target.
# Our first base case is when the sorted list is empty.
# Within binary_search(), use a conditional to check whether the list is empty.
# If it is, return "value not found".
def binary_search(sorted_list, target):
  if not sorted_list:
    return "value not found"
  # We’ll set up our recursive step.
  # Declare two variables: mid_idx and mid_val.
  # mid_idx should be the middle index of sorted_list.
  # mid_val is the value located in sorted_list at the mid_idx.
  # return these two variables like so: return mid_idx, mid_val
  mid_idx = len(sorted_list) // 2
  mid_val = sorted_list[mid_idx]
  return mid_idx, mid_val

# For testing:
sorted_values = [13, 14, 15, 16, 17]
print(binary_search([], 42))
print(binary_search(sorted_values, 42))