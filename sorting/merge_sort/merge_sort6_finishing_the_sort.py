# Finishing the Sort

# Let’s update our merge_sort() function so that it returns a sorted list finally!

def merge_sort(items):
  if len(items) <= 1:
    return items

  middle_index = len(items) // 2
  left_split = items[:middle_index]
  right_split = items[middle_index:]
  # In merge_sort() create two new variables: left_sorted and right_sorted.
  # left_sorted should be the result of calling merge_sort() recursively on left_split.
  # right_sorted should be the result of calling merge_sort() recursively on right_split.
  left_sorted = merge_sort(left_split)
  right_sorted = merge_sort(right_split)
  # Erase the “return” line and change it to return the result of calling merge() on left_sorted and right_sorted.
  #return middle_index, left_split, right_split
  return merge(left_sorted, right_sorted)

def merge(left, right):
  result = []

  while (left and right):
    if left[0] < right[0]:
      result.append(left.pop(0))
    else:
      result.append(right.pop(0))

  if left:
    result += left
  if right:
    result += right

  return result