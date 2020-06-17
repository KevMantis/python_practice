# Larger Sum

# Create a function named larger_sum() that takes two lists of numbers as parameters named lst1 and lst2.

# The function should return the list whose elements sum to the greater number. If the sum of the elements of each list are equal, return lst1.

def larger_sum(lst1, lst2):
  lst1_sum = 0
  lst2_sum = 0
  for n1 in lst1:
    lst1_sum += n1
  for n2 in lst2:
    lst2_sum += n2
  if lst2_sum > lst1_sum:
    return lst2
  else:
    return lst1

print(larger_sum([1, 9, 5], [2, 3, 7]))
