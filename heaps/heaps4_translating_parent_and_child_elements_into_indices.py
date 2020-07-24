# Translating Parent and Child Elements Into Indices

# Great work so far! Our MinHeap adds elements to the internal list, keeps a running count, and has the beginnings of .heapify_up().
# Before we dive into the logic for .heapify_up(), let’s review how heaps track elements. We use a list for storing internal elements, but we’re modeling it on a binary tree, where every “parent” element has up to two “child” elements.
# “child” and “parent” elements are determined by their relative indices within the internal list. By doing some arithmetic on an element’s index, we can determine the indices for parent and child elements (if they exist).
# - Parent: index // 2
# - Left Child: index * 2
# - Right Child: (index * 2) + 1
#  print(heap.heap_list)
#  #        [None, 10, 13, 21, 61, 22, 23, 99]
#  # Indices: [0, 1, 2, 3, 4, 5, 6, 7]
#  
#  heap.parent_idx(4)
#  # (4 // 2) == 2
#  # Element at index 4 is 61 
#  # Element at index 2 is 13
#  # The parent element of 61 is 13
#  
#  heap.left_child(3)
#  # (3 * 2) == 6
#  # Element at index 3 is 21
#  # Element at index 6 is 23
#  # The left child element of 21 is 23
# These calculations are important for the efficiency of the heap, but they’re not necessary to memorize, so we’ve added three helper methods: .parent_idx(), .left_child_idx(), and .right_child_idx().
# These helpers take an index as the argument and return the corresponding parent or child index.

# Fill in the code in script.py to test out these new helper methods.

# importing heap class
from min_heap import MinHeap 

# an instance of MinHeap to use
min_heap = MinHeap()

# the internal list for our example
min_heap.heap_list = [None, 10, 13, 21, 61, 22, 23, 99]
print(min_heap.heap_list)


# example of how to use the helper methods:
print("the parent index of 4 is:")
print(min_heap.parent_idx(4))
print("the left child index of 3 is:")
print(min_heap.left_child_idx(3))

# now it's your turn!
# replace 'None' below using the correct helper methods and indexes
idx_2_left_child_idx = min_heap.left_child_idx(2)
print("The left child index of index 2 is:")
print(idx_2_left_child_idx)
print("The left child element of index 2 is:")
# uncomment the line below to see the result in your console!
print(min_heap.heap_list[idx_2_left_child_idx])

idx_3_parent_idx = min_heap.parent_idx(3)
print("The parent index of index 3 is:")
print(idx_3_parent_idx)
print("The parent element of index 3 is:")
# uncomment the line below to see the result in your console!
print(min_heap.heap_list[idx_3_parent_idx])

idx_3_right_child_idx = min_heap.right_child_idx(3)
print("The right child index of index 3 is:")
print(idx_3_right_child_idx)
print("The right child element of index 3 is:")
# uncomment the line below to see the result in your console!
print(min_heap.heap_list[idx_3_right_child_idx])