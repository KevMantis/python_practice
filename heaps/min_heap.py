# Within min_heap.py, define the MinHeap class. Use a constructor that only takes self as an argument.
# Inside the constructor, assign a list containing None to self.heap_list and 0 to self.count.
class MinHeap:
  def __init__(self):
    self.heap_list = [None]
    self.count = 0

  # HEAP HELPER METHODS
  # DO NOT CHANGE!
  def parent_idx(self, idx):
    return idx // 2

  def left_child_idx(self, idx):
    return idx * 2

  def right_child_idx(self, idx):
    return idx * 2 + 1

  # NEW HELPER!
  def child_present(self, idx):
    return self.left_child_idx(idx) <= self.count

  # END OF HEAP HELPER METHODS

  # Define a .retrieve_min() method within our MinHeap class. Its only parameter is self.
  # Check if our internal count is at 0…  
  # If it is, we have no elements to retrieve, so print a friendly “No items in heap” and return None.
  def retrieve_min(self):
    if self.count == 0:
      print("No items in heap")
      return
      # Declare the variable min, which is the element at index 1 in our internal list.
    min = self.heap_list[1]
    # Print the message “Removing: min from self.heap_list“.
    # Then, swap the element at index 1 with the last element in the internal list.
    # Remove the last element from the list, and decrement the count.
    self.heap_list[1] = self.heap_list[self.count]
    self.heap_list.pop()
    self.count -= 1
    # Print the message “Last element moved to first: self.heap_list“.
    # Finally, return the min variable.
    print("Last element moved to first: {}".format(self.heap_list))
    # Go back into .retrieve_min() and fix the method by calling .heapify_down() before we return min.
    self.heapify_down()
    return min

  # Define .heapify_down() on MinHeap, its only parameter is self.
  # Print “Heapifying down!”.
  def heapify_down(self):
    print("Heapifying down!")
    # Declare a variable idx and set it to 1.
    # Initially, this is pointing to our out-of-place value we swapped in while removing the minimum.
    idx = 1
    # Inside of .heapify_down(), open up a while loop after your idx declaration.
    # The loop should run as long as idx has a child element. Use the new helper method: .child_present().
    # Print “Heapifying down!” within the loop.
    while self.child_present(idx):
      print("Heapifying down!")
      # Inside the loop, declare the variable smaller_child_idx and set it equal to the appropriate value.
      smaller_child_idx = self.get_smaller_child_idx(idx)
      # Declare two variables: child and parent, set to the appropriate element from the internal list using smaller_child_idx and idx.
      child = self.heap_list[smaller_child_idx]
      parent = self.heap_list[idx]
      # Check if parent is greater than child. If it is, we’ll need to make a swap.
      if parent > child:
        self.heap_list[idx] = child
        self.heap_list[smaller_child_idx] = parent
      # Finish the loop by setting idx equal to smaller_child_idx. This is how we’ll terminate the loop, by moving down through the “tree” until there are no “child” elements to consider.
      # Outside the loop, print “Heap Restored! self.heap_list“.
      idx = smaller_child_idx
    print("Heap restored! {}".format(self.heap_list))

  # Inside min_heap.py, define .add() within Heap. .add() takes two arguments: self and element.
  # Give users a helpful print message like “Adding element to self.heap_list.”
  def add(self, element):
    print("Adding {} to {}".format(element, self.heap_list))
    # Inside of .add(), increment the internal element count, then add the element to the end of the internal list.
    self.count += 1
    self.heap_list.append(element)
    # Finish .add() by calling the .heapify_up() method we just defined.
    self.heapify_up()

  # Define .get_smaller_child_idx(), it will take self and idx as arguments.
  # Check if we have a right child for this index. We don’t if the right child index is greater than our internal count.
  # If we don’t, print “There is only a left child” and return the left child index.
  def get_smaller_child_idx(self, idx):
    if self.right_child_idx(idx) > self.count:
      print("There is only a left child")
      return self.left_child_idx(idx)
    # If we do have a right child, we need to make a comparison to see which is smaller.
    # Declare left_child and right_child as variables and assign them to the appropriate elements from the internal list.
    # You can do this by using helper methods .left_child_idx() and .right_child_idx() to access elements in self.heap_list.
    left_child = self.heap_list[self.left_child_idx(idx)]
    right_child = self.heap_list[self.right_child_idx(idx)]
    # Make another conditional for the comparison between left_child and right_child.
    # If the left child is smaller, print a message saying so and return the index of the left child.
    # Else, do the same but for the right child.
    if left_child < right_child:
      print("{} is less than {}".format(left_child, right_child))
      return self.left_child_idx(idx)
    else:
      print("{} is less than {}".format(right_child, left_child))
      return self.right_child_idx(idx)

  # Define another method inside MinHeap: .heapify_up(). It has self as a parameter.
  # Print out the message “Restoring the heap property…” within .heapify_up().
  def heapify_up(self):
    print("Restoring the heap property...")
    # Inside of .heapify_up(), declare a variable called idx and set it to the last index of the internal list.
    idx = self.count
    # Set up a while loop that will run as long as there is a valid parent index. A valid parent index is anything greater than 0.
    # Inside the loop, set idx to be the index of its parent.
    # This will be the last part of the loop, but we’re writing it first so we don’t get stuck in infinite loops.
    while self.parent_idx(idx) > 0:
      # At the beginning of the loop, declare a variable child and set it equal to the element in the internal list at idx.
      # Declare another variable parent and set it equal to the element in the internal list at self.parent_idx(idx).
      # Check to see if parent is greater than child.
      # If it is greater, print the message: “swapping parent_element with element_at_index“.
      child = self.heap_list[idx]
      parent = self.heap_list[self.parent_idx(idx)]
      if parent > child:
        print("swapping {} with {}".format(parent, self.heap_list[idx]))
        # If the parent element is larger than the element at idx, we need to swap to restore the heap properties.
        # Swap the elements by setting the value at idx to be parent and the value at self.parent_idx(idx) to be child!
        self.heap_list[idx] = parent
        self.heap_list[self.parent_idx(idx)] = child
      idx = self.parent_idx(idx)
    # When the loop ends, congratulations, you’ve restored your heap.
    # Print the message “Heap Restored self.heap_list“
    # Tab over to script.py and run the code to enjoy the fruits of your labor!
    print("Heap Restored {}".format(self.heap_list))