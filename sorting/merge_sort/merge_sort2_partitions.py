# Partitions

# How do we break up the data in a merge sort? We split it in half until there’s no more data to split. Our first step is to break down all of the items of the list into their own list.

def merge_sort(items):
  if len(items) <= 1:
    return items
  # After returning all inputs that have less than 2 elements, we split everything up that’s longer.
  # Create the variable middle_index which is the index to the middle element in the list.
  middle_index = len(items) // 2
  # Create another variable called left_split. This should be a list of all elements in the input list starting at the first up to but not including the middle_index element.
  left_split = items[:middle_index]
  # Create one more variable called right_split which includes all elements in items from the middle_index to the end of the list.
  right_split = items[middle_index:]
  # For now, return all three of these at the bottom of the function in a single return statement. Like this:
  """
  return middle_index, left_split, right_split
  """
  return middle_index, left_split, right_split