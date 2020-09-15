# Recursive Binary Search: Review and Refactor

# Congratulations, you implemented a version of the binary search algorithm using recursion!
# Let’s recap how we solved this problem:
# 1. We know our inputs will be sorted, which helps us make assertions about where to search for values.
# 2. We divide the list in half and compare our target value with the middle element.
# 3. If they match, we return the index
# 4. If they don’t match, we begin again at the first step with the appropriate half of the original list.
# 5. When the list is empty, the target is not found.
# Our original solution solved the problem of reducing the sorted input list by making a smaller copy of the list.
# This is wasteful! At each recursive call we’re copying N/2 elements where N is the length of the sorted list.
# We can do better by using pointers instead of copying the list. Pointers are indices stored in a variable that mark the beginning and end of a list:
"""
vehicles = ["car", "jet", "camel", "boat"]
start_of_list = 0
end_of_list = len(vehicles)
# 4

vehicles[start_of_list : end_of_list]
# ["car", "jet", "camel", "boat"]

middle_of_list = len(vehicles) // 2
# 2

vehicles[start_of_list : middle_of_list]
# ["car", "jet"]
vehicles[middle_of_list : end_of_list]
# ["camel", "boat"]

# This example copies the list to show what portion is covered
# We won't need to copy in the algorithm!
"""
# With pointers, we’ll track which sub-list we’re searching within the original input and there’s no need for copying.
# Our overall strategy is the same, but we’ll need to change the following sections:
# - binary_search() has two parameters
#   - It should have four
# - Our base case checks for an empty list
#   - It should check whether the pointers indicate an empty sub-list
# - Our recursive calls use copied sub-lists
#   - They should update the pointers to indicate which portion of the list we’re searching.
# - Our “right-half” recursive calls do some arithmetic.
#   - That’s no longer necessary!

def binary_search(sorted_list, left_pointer, right_pointer, target):
  # this condition indicates we've reached an empty "sub-list"
  if left_pointer >= right_pointer:
    return "value not found"
	
  # We calculate the middle index from the pointers now
  mid_idx = (left_pointer + right_pointer) // 2
  mid_val = sorted_list[mid_idx]

  if mid_val == target:
    return mid_idx
  if mid_val > target:
    # we reduce the sub-list by passing in a new right_pointer
    return binary_search(sorted_list, left_pointer, mid_idx, target)
  if mid_val < target:
    # we reduce the sub-list by passing in a new left_pointer
    return binary_search(sorted_list, mid_idx + 1, right_pointer, target)
  
values = [77, 80, 102, 123, 288, 300, 540]
start_of_values = 0
end_of_values = len(values)
result = binary_search(values, start_of_values, end_of_values, 288)

print("element {0} is located at index {1}".format(288, result))