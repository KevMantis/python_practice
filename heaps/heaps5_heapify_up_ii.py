# Adding an Element: Heapify Up II

# Now that we understand how to determine the relationship of elements with the internal list, we’re ready to finish .heapify_up().
# We need to make sure that every child is greater in value than their parent. Say we add an element to the following heap:
#  print(heap.heap_list)
#  # [None, 10, 13, 21, 61, 22, 23, 99]
#  heap.add(12)
#  
#  # ( new_element )
#  # { parent_element }
#  # [None, 10, 13, 21, {61}, 22, 23, 99, (12)]
# Oh no! We’ve violated the heap property: 12‘s parent is 61, the parent element is greater than the child.
# Don’t fret; we can fix this. We’ll exchange the parent and the child elements.
#  # [None, 10, 13, 21, {61}, 22, 23, 99, (12)]
#  # SWAP 12 and 61
#  # [None, 10, 13, 21, (12), 22, 23, 99, {61}]
# 12‘s parent is now 13, they’re close but the parent element is still greater than the child. Keep on swappin’!
#  # [None, 10, {13}, 21, (12), 22, 23, 99, 61]
#  # SWAP 12 and 13
#  # [None, 10, (12), 21, {13}, 22, 23, 99, 61]
# Okay, you can let out that sigh of relief. We’ve restored the heap properties!
#  # [None, {10}, (12), 21, 13, 22, 23, 99, 61]
#  # The child, 12, is greater than the parent, 10!
# Let’s recap our strategy for .heapify_up():
#  # start at the last element of the list
#  # while there's a parent element available:
#    # if the parent element is greater:
#      # swap the elements
#    # set the target element index to be the parent's index

# Inside of .heapify_up(), declare a variable called idx and set it to the last index of the internal list.

# Set up a while loop that will run as long as there is a valid parent index. A valid parent index is anything greater than 0.
# Inside the loop, set idx to be the index of its parent.
# This will be the last part of the loop, but we’re writing it first so we don’t get stuck in infinite loops.

# At the beginning of the loop, declare a variable child and set it equal to the element in the internal list at idx.
# Declare another variable parent and set it equal to the element in the internal list at self.parent_idx(idx).
# Check to see if parent is greater than child.
# If it is greater, print the message: “swapping parent_element with element_at_index“.

# If the parent element is larger than the element at idx, we need to swap to restore the heap properties.
# Swap the elements by setting the value at idx to be parent and the value at self.parent_idx(idx) to be child!

# When the loop ends, congratulations, you’ve restored your heap.
# Print the message “Heap Restored self.heap_list“
# Tab over to script.py and run the code to enjoy the fruits of your labor!

# import random number generator
from random import randrange
# import heap class
from min_heap import MinHeap 

# make an instance of MinHeap
min_heap = MinHeap()

# populate min_heap with random numbers
random_nums = [randrange(1, 101) for n in range(6)]
for el in random_nums:
  min_heap.add(el)


# test it out, is the minimum number at index 1?
print(min_heap.heap_list)
