# Merging

# Now we need to build out our result list. When we’re merging our lists together, we’re creating ordered lists that combine the elements of two lists.

def merge_sort(items):
  if len(items) <= 1:
    return items

  middle_index = len(items) // 2
  left_split = items[:middle_index]
  right_split = items[middle_index:]

  return middle_index, left_split, right_split

def merge(left, right):
  result = []
  # Since we’re going to be removing the contents of each list until they’re both depleted, let’s start with a while loop!
  # Create a loop that will continue iterating while both left and right have elements. When one of those two are empty we’ll want to move on.
  while (left and right):
    # Now we do our comparison! Check if the first element (index 0, remember) of left is smaller than the first element of right.
    if left[0] < right[0]:
      # If left[0] is smaller than right[0], we want to add it to our result! Append left[0] to our result list.
      # Since we’ve added it to our results we’ll want to remove it from left. Use left.pop() to remove the first element from the left list.
      result.append(left.pop(0))
    # If left[0] is larger than right[0], we want to add right[0] to our result! Append right[0] to result and then pop it out of right.
    else:
      result.append(right.pop(0))
  return result