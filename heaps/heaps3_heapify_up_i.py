# Adding an Element: Heapify Up I

# The min-heap is no good if all it ever contains is None. Let’s build the functionality to add elements while maintaining the heap properties.
# Our MinHeap will abide by two principles:
# - The element at index 1 is the minimum value in the entire list.
# - Every “child” element in the list must be larger than their “parent”.
# The first element we add to the list will be the minimum because there are no other elements. We’ll tackle the trickier aspects of maintaining these principles in the coming lessons.
# For now, let’s define .add() which will allow us to add elements into the .heap_list. We’ll also start defining .heapify_up(), which will do the work of maintaining the heap properties as we add additional elements.

# Inside min_heap.py, define .add() within Heap. .add() takes two arguments: self and element.
# Give users a helpful print message like “Adding element to self.heap_list.”

# Inside of .add(), increment the internal element count, then add the element to the end of the internal list.

# Run the test code within script.py to see the element 42 added to the internal list.

# Define another method inside MinHeap: .heapify_up(). It has self as a parameter.
# Print out the message “Restoring the heap property…” within .heapify_up().

# Finish .add() by calling the .heapify_up() method we just defined.
# Run the test code in script.py.

# import heap class
from min_heap import MinHeap 

min_heap = MinHeap()
print(min_heap.heap_list)

# testing out .add()
min_heap.add(42)
print(min_heap.heap_list)