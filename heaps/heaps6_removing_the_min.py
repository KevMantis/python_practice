# Removing the Min

# Min-heaps would be useless if we couldn’t retrieve the minimum value. We’ve gone through a lot of work to maintain that value because we’re going to need it!
# Our goal is to efficiently remove the minimum element from the heap. You’ll recall that we always locate the minimum element at index 1, (a sentinel element occupies index 0).
# Our internal list mirrors a binary tree. There’s a delicate balance of parent and child relationships we would ruin by directly removing the minimum.
#  print(heap.heap_list)
#  # [None, 10, 21, 13, 61, 22, 23, 99]
#  heap.retrieve_min()
#  # 10
#  # [None, ???, 21, 13, 61, 22, 23, 99]
# We need to remove an element that has no children; we need to remove the last element. Swap the minimum with the last element, and we can easily remove the minimum from the end of the list.
#  # [None, (10), 21, 13, 61, 22, 23, {99}]
#  heap.retrieve_min()
#  # [None, {99}, 21, 13, 61, 22, 23, (10)]
#  # [None, 99, 21, 13, 61, 22, 23]
#  # 10
# Terrific! We removed the minimum element with minimal disruption. Unfortunately, our heap is out of shape again with 99 sitting where the minimum element should be.
# Patience, young Heap-prentice. We will solve this in lessons to come…

# Define a .retrieve_min() method within our MinHeap class. Its only parameter is self.
# Check if our internal count is at 0…
# If it is, we have no elements to retrieve, so print a friendly “No items in heap” and return None.

# Declare the variable min, which is the element at index 1 in our internal list.

# Print the message “Removing: min from self.heap_list“.
# Then, swap the element at index 1 with the last element in the internal list.
# Remove the last element from the list, and decrement the count.

# Print the message “Last element moved to first: self.heap_list“.
# Finally, return the min variable.

# Tab over to script.py and run the test code.

# import heap class
from min_heap import MinHeap 

# make an instance of MinHeap
min_heap = MinHeap()

# add elements
min_heap.add(7)
min_heap.add(12)
min_heap.add(42)

# remove minimum element
print(min_heap.retrieve_min())