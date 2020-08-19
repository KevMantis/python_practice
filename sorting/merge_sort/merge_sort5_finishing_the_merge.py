# Finishing the Merge

# Since we’ve only technically depleted one of our two inputs to merge(), we want to add in the rest of the values to finish off our merge() function and return the sorted list.

def merge_sort(items):
  if len(items) <= 1:
    return items

  middle_index = len(items) // 2
  left_split = items[:middle_index]
  right_split = items[middle_index:]

  return middle_index, left_split, right_split

def merge(left, right):
  result = []

  while (left and right):
    if left[0] < right[0]:
      result.append(left.pop(0))
    else:
      result.append(right.pop(0))
  # After our while loop, check if there are any elements still in left.
  # If there are, add those elements to the end of result.
  if left:
    result += left
  # After checking for elements in left let’s check if there are elements in right. If there are, add them to result.
  if right:
    result += right
  return result