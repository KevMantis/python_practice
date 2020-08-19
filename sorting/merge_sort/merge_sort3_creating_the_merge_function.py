# Creating the Merge Function

# Our merge_sort() function so far only separates the input list into many different parts — pretty much the opposite of what you’d expect a merge sort to do. To actually perform the merging, we’re going to define a helper function that joins the data together.

def merge_sort(items):
  if len(items) <= 1:
    return items

  middle_index = len(items) // 2
  left_split = items[:middle_index]
  right_split = items[middle_index:]

  return middle_index, left_split, right_split

# Define the function merge(), which is going to take care of merging our two lists together. It should take two parameters: left and right. These are going to be the two (sorted) lists we want to merge.
def merge(left, right):
  # Instantiate a new empty list and call it result. We’re going to add members of left and right to result until it contains a sorted list with all elements of both.
  # Return result at the end of the function.
  result = []
  return result