# Min-Heaps of Fun

# We’re going to implement a min-heap in Python. Min-heaps efficiently keep track of the minimum value in a dataset, even as we add and remove elements.
# Min-heaps are nearly identical to a max-heap, just with the comparisons reversed. It’s a two for one lesson!
# Heaps enable solutions for complex problems such as finding the shortest path (Dijkstra’s Algorithm) or efficiently sorting a dataset (heapsort).
# They’re an essential tool for confidently navigating some of the difficult questions posed in a technical interview.
# By understanding the operations of a heap, you will have made a valuable addition to your problem-solving toolkit.

# import random number generator
from random import randrange
# import heap class
from min_heap1 import MinHeap 

# make an instance of MinHeap
min_heap = MinHeap()

# populate min_heap with random numbers
random_nums = [randrange(1, 101) for n in range(6)]
for el in random_nums:
  min_heap.add(el)

# remove minimum until min_heap is empty
while min_heap.count != 0:
  min_heap.retrieve_min()
