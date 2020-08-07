# Recursive Data Structures

# Data structures can also be recursive.
# Trees are a recursive data structure because their definition is self-referential. A tree is a data structure which contains a piece of data and references to other trees!
# Trees which are referenced by other trees are known as children. Trees which hold references to other trees are known as the parents.
# A tree can be both parent and child. We’re going to write a recursive function that builds a special type of tree: a binary search tree.
# Binary search trees:
#   - Reference two children at most per tree node.
#   - The “left” child of the tree must contain a value lesser than its parent
#   - The “right” child of the tree must contain a value greater than its parent.
# Trees are an abstract data type, meaning we can implement our version in a number of ways as long as we follow the rules above.
# For the purposes of this exercise, we’ll use the humble Python dictionary:
"""
bst_tree_node = {"data": 42}
bst_tree_node["left_child"] = {"data": 36}
bst_tree_node["right_child"] = {"data": 73}

bst_tree_node["data"] > bst_tree_node["left_child"]["data"]
# True
bst_tree_node["data"] < bst_tree_node["right_child"["data"]
# True
"""
# We can also assume our function will receive a sorted list of values as input.
# This is necessary to construct the binary search tree because we’ll be relying on the ordering of the list input.
# Our high-level strategy before moving through the checkpoints.
#   1. base case: the input list is empty
#     2. Return "No Child" to represent the lack of node
#   3. recursive step: the input list must be divided into two halves
#     4. Find the middle index of the list
#     5. Store the value located at the middle index
#     6. Make a tree node with a "data" key set to the value
#     7. Assign tree node’s "left child" to a recursive call using the left half of the list
#     8. Assign tree node’s "right child" to a recursive call using the right half of the list
#     9. Return the tree node

# Define the build_bst() function with my_list as the sole parameter.
# If my_list has no elements, return “No Child” to represent the lack of a child tree node.
# This is the base case of our function.
# The recursive step will need to remove an element from the input to eventually reach an empty list.
def build_bst(my_list):
  if len(my_list) == 0:
    return 'No Child'
  # We’ll be building this tree by dividing the list in half and feeding those halves to the left and right sides of the tree.
  # This dividing step will eventually produce empty lists to satisfy the base case of the function.
  # Outside of the conditional you just wrote, declare middle_idx and set it to the middle index of my_list.
  # Then, declare middle_value and set it to the value in my_list located at middle_idx.
  # Print “Middle index: “ + middle_idx.
  # Then, print “Middle value: “ + middle_value
  # You can use .format() or addition for the print the statement. Addition will require you to use str() on the variables since they are integers!
  middle_idx = len(my_list) // 2
  middle_value = my_list[middle_idx]
  print('Middle index: {}'.format(middle_idx))
  print('Middle value: {}'.format(middle_value))
  # After the print statements, declare the variable tree_node that points to a Python dictionary with a key of "data" pointing to middle_value.
  # tree_node represents the tree being created in this function call. We want a tree_node created for each element in the list, so we’ll repeat this process on the left and right sub-trees using the appropriate half of the input list.
  # Now for the recursive calls!
  # Set the key of "left_child" in tree_node to be a recursive call to build_bst() with the left half of the list not including the middle value as an argument.
  # Set the key of "right_child" in tree_node to be a recursive call to build_bst() with the right half of the list not including the middle value as an argument.
  # It’s very important we don’t include the middle_value in the lists we’re passing as arguments, or else we’ll create duplicate nodes!
  # Finally, return tree_node. As the recursive calls resolve and pop off the call stack, the final return value will be the root or “top” tree_node which contains a reference to every other tree_node.
  tree_node = {"data": middle_value}
  tree_node['left_child'] = build_bst(my_list[:middle_idx])
  tree_node['right_child'] = build_bst(my_list[middle_idx + 1:])
  return tree_node

# For testing
sorted_list = [12, 13, 14, 15, 16]
binary_search_tree = build_bst(sorted_list)
print(binary_search_tree)

# Congratulations! You’ve built up a recursive data structure with a recursive function!
# This data structure can be used to find values in an efficient O(logN) time.
# Fill in the variable runtime with the runtime of your build_bst() function.
# This runtime is a tricky one so don’t be afraid to use that hint!

# fill in the runtime as a string
# 1, logN, N, N*logN, N^2, 2^N, N!
runtime = "N*logN"