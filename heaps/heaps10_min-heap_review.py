# Min-Heap Review

# Nice work! You’ve implemented a min-heap in Python, and that’s no small feat (although it could efficiently track the smallest feat).
# To recap: MinHeap tracks the minimum element as the element at index 1 within an internal Python list.
# When adding elements, we use .heapify_up() to compare the new element with its parent, making swaps if it violates the heap property: children must be greater than their parents.
# When removing the minimum element, we swap it with the last element in the list. Then we use .heapify_down() to compare the new root with its children, swapping with the smaller child if necessary.
# Heaps are so useful because they’re efficient in maintaining their heap properties. Building a heap using elements that decreased in value would ensure that we continually violated the heap property. How many swaps would that cause?

# Run the code in script.py to see how many swaps are made in a dataset of 10,000 elements!

# import random number generator
from random import randrange
# import heap class
from min_heap2 import MinHeap 

# make an instance of MinHeap
min_heap = MinHeap()

# populate min_heap with descending numbers
descending_nums = [n for n in range(10001, 1, -1)]
print("ADDING!")
for el in descending_nums:
  min_heap.add(el)

print("REMOVING!")
# remove minimum until min_heap is empty
min_heap.retrieve_min()
