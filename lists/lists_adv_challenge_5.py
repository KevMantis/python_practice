# 5. Middle Item

# Create a function called middle_element that has one parameter named lst.

# If there are an odd number of elements in lst, the function should return the middle element. If there are an even number of elements, the function should return the average of the middle two elements.

def middle_element(lst):
  if (len(lst) % 2) == 0:
    middle2 = int(len(lst) / 2)
    even_slice = lst[middle2-1:middle2+1]
    middle2_average = sum(even_slice) / len(even_slice)
    return middle2_average
  else:
    middle1 = int(len(lst) / 2)
    return lst[middle1]
print(middle_element([5, 2, -10, -4, 4, 5]))
