# Removing the Min: Heapify Down II

# We’ve got a handy helper to tell us which child element is smaller, so there’s nothing standing between us and a pristine heap.
# As a reminder, our strategy will be very similar to .heapify_up(), but we’ll be moving down the tree. Here’s the general shape of the method:
#   # starting with our first element...
#   # while there's at least one child present:
#     # get the smallest child's index
#     # compare the smallest child with our element
#       # if our element is larger, swap with child
#     # regardless, set our element index to be the child
# We’ve added another helper method for you: .child_present(). This returns a boolean indicating whether a given index has an associated child element. Use it wisely…

# Inside of .heapify_down(), open up a while loop after your idx declaration.
# The loop should run as long as idx has a child element. Use the new helper method: .child_present().
# Print “Heapifying down!” within the loop.

# Inside the loop, declare the variable smaller_child_idx and set it equal to the appropriate value.

# Declare two variables: child and parent, set to the appropriate element from the internal list using smaller_child_idx and idx.

# Check if parent is greater than child. If it is, we’ll need to make a swap.

# Finish the loop by setting idx equal to smaller_child_idx. This is how we’ll terminate the loop, by moving down through the “tree” until there are no “child” elements to consider.
# Outside the loop, print “Heap Restored! self.heap_list“.
# Tab over to script.py and test it out.

# import heap class
from min_heap import MinHeap 

# make an instance of MinHeap
min_heap = MinHeap()

# set internal list for testing purposes...
min_heap.heap_list = [None, 10, 13, 21, 61, 22, 23, 99]
min_heap.count = 7

while len(min_heap.heap_list) != 1:
  print(min_heap.heap_list)
  min_heap.retrieve_min()