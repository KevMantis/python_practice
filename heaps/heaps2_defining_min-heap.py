# Defining Min-Heap

# Our MinHeap class will store two pieces of information:
# - A Python list of the elements within the heap.
# - A count of the elements within the heap.
# To make our lives easier, we’ll always keep one sentinel element at the beginning inside the list: None.
#  heap = MinHeap()
#  print(heap.heap_list)
#  # [None]
#  print(heap.count)
#  # 0
# This dummy value will save us the trouble of checking whether the list is empty and simplify the methods we define in later lessons.

# Within min_heap.py, define the MinHeap class. Use a constructor that only takes self as an argument.
# Inside the constructor, assign a list containing None to self.heap_list and 0 to self.count.

from min_heap import MinHeap 

# Tab over to script.py. Make an instance of MinHeap and assign it to the variable heap.
# Print out heap.heap_list.
# Run your code!
heap = MinHeap()
print(heap.heap_list)