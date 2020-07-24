# Finding the Smallest Child

# We mentioned .heapify_down() is a lot like .heapify_up(). We’ll track an offending element in the heap, and keep swapping it with another element until we’ve restored the heap properties.
# The wrinkle is .heapify_down() gives us another option for which element to swap. In .heapify_up(), we were always comparing our element with its parent. In .heapify_down(), we have potentially two options: the left child and the right child.
# Which should we choose? We’ll use an example to think it through. Imagine we have a heap with four elements:
#  print(heap.heap_list)
#  # [None, 21, 36, 58, 42]
#  heap.retrieve_min()
#  # 21
#  # [None, 42, 36, 58]
#  # Should we swap with 36 or 58?
# We want to swap with the smaller of the two children, otherwise, we wouldn’t maintain our heap properties!
# Let’s write a helper method to determine the smallest child element for a given index. We’ll make heavy use of our other helper methods: .left_child_idx() and .right_child_idx().
# .get_smaller_child_idx() will have the following structure:
#  # check if we have a right child
#    # if we don't, return the left child index
#    # if we do...
#      # return the index of the smaller child

# Define .get_smaller_child_idx(), it will take self and idx as arguments.
# Check if we have a right child for this index. We don’t if the right child index is greater than our internal count.
# If we don’t, print “There is only a left child” and return the left child index.

# If we do have a right child, we need to make a comparison to see which is smaller.
# Declare left_child and right_child as variables and assign them to the appropriate elements from the internal list.
# You can do this by using helper methods .left_child_idx() and .right_child_idx() to access elements in self.heap_list.

# Make another conditional for the comparison between left_child and right_child.
# If the left child is smaller, print a message saying so and return the index of the left child.
# Else, do the same but for the right child.

# Tab over to script.py and test out this new method by replacing None with the correct index value.

# import random number generator
from random import randrange
# import heap class
from min_heap import MinHeap 

# make an instance of MinHeap
min_heap = MinHeap()

# set internal list for testing purposes...
min_heap.heap_list = [None, 10, 13, 21, 61, 22, 23, 99]
min_heap.count = 7

print("The smaller child of index 1 is: ")
smaller_child_of_idx_1 = min_heap.get_smaller_child_idx(1)
smaller_child_element = min_heap.heap_list[smaller_child_of_idx_1]
print(smaller_child_element)

print("The smaller child of index 2 is: ")
smaller_child_of_idx_2 = min_heap.get_smaller_child_idx(2)
smaller_child_element = min_heap.heap_list[smaller_child_of_idx_2]
print(smaller_child_element)

print("The smaller child of index 3 is: ")
smaller_child_of_idx_3 = min_heap.get_smaller_child_idx(3)
smaller_child_element = min_heap.heap_list[smaller_child_of_idx_3]
print(smaller_child_element)
