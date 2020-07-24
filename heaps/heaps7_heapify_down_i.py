# Heapify Down I

# We’ve retrieved the minimum element but left our MinHeap in disarray. There’s no reason to get discouraged, we’ve handled this type of problem before, and we can get our MinHeap back in shape!
# We’ll define a method, .heapify_down(), which performs a similar role to .heapify_up(), except now we’re moving down the “tree” instead of up.

# Define .heapify_down() on MinHeap, its only parameter is self.
# Print “Heapifying down!”.

# Declare a variable idx and set it to 1.
# Initially, this is pointing to our out-of-place value we swapped in while removing the minimum.

# Go back into .retrieve_min() and fix the method by calling .heapify_down() before we return min.

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

# Test that .heapify_down() is called by .retrieve_min()
min_heap.retrieve_min()