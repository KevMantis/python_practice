# 2. Larger List

# Write a function named larger_list that has two parameters named lst1 and lst2.

# The function should return the last element of the list that contains more elements. If both lists are the same size, then return the last element of lst1.

def larger_list(lst1,lst2):
  len_lst1 = len(lst1)
  len_lst2 = len(lst2)
  if len_lst2 > len_lst1:
    return lst2[-1]
  else:
    return lst1[-1]
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))
